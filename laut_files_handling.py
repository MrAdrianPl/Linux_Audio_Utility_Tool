
def LoadPwJson(prefix,configuration):

    file_data_str = ""
    with open(prefix + configuration, 'r') as file:
            stripped_lines = (line.rstrip() for line in file)
            for lines in stripped_lines:
                    if not lines.lstrip().startswith('#') and lines:
                            file_data_str +=(lines.split('#')[0] + '\n')

    main = []
    ins = []

    sqr_indx = 0
    brack_index = 0
    for line in file_data_str.split('\n'):
            if '{' in line:
                    brack_index += 1
                    if brack_index == 1:
                            if line.strip().startswith('{'):
                                    main.append(line.split('=')[0].strip()[2:])
                            else:
                                    main.append(line.split('=')[0].strip())

                    if brack_index > 1:
                            ins.append(line.strip())
            if '{' not in line and '}' not in line:
                    ins.append(line.strip())
            if '{' in line and '}' in line:
                    ins.append(line.split('=')[-1].strip()[:-3])
            if '}' in line:
                    brack_index += -1
                    if brack_index > 0:
                            ins.append(line.split('=')[-1].strip())
                    if brack_index == 0:
                            main.append(ins)
                            ins = []
            if brack_index == 0 and '[' in line:
                    sqr_indx += 1
                    brack_index += 1
                    main.append(line.split('=')[0].strip())
                    ins = []
            if sqr_indx > 0 and brack_index == 1 and ']' in line and '[' not in line:
                    sqr_indx += -1
                    brack_index += -1
                    if brack_index == 0:
                            main.append(ins)
                            ins = []
    return main

def CreateConfigFilePipeWire(params_list:dict):
        template = f"""
        context.properties = {{
        link.max-buffers = { params_list["max-buffers"] or 16 }
        default.clock.rate          = { params_list["clock-rate"] }
        default.clock.allowed-rates = { params_list["allowed-rates"] }
        default.clock.quantum       = { params_list["quantum-def"] }
        default.clock.min-quantum   = { params_list["quantum-min"] }
        default.clock.max-quantum   = { params_list["quantum-max"] }
        default.clock.quantum-limit = { params_list["quantum-limit"] }
        }}
        """
        return template

def findMatchingSettings(input_list):
        occ_index = [ index for index,content in enumerate(input_list) if content.startswith('matches = [') ]
        start_index = [ index - 1 for index in occ_index ]
        end_index = [index for index,content in enumerate(input_list) if content == '}' and index in occ_index ]

        return

def CreateConfigFilePipeWirePulse(params_list:dict):
        template = f"""
        stream.properties = {{

        node.latency =          { params_list["node-latency-param"] }
        resample.quality =      { params_list["resample-quality-param"] }

        }}
        pulse.properties = {{
                pulse.min.req           = { params_list["pulse-min-req"] }/{ params_list["arbitrary-sampling-param"] }
                pulse.default.req       = { params_list["pulse-default-req"] }/{ params_list["arbitrary-sampling-param"] }
                pulse.min.frag          = { params_list["pulse-min-frag"] }/{ params_list["arbitrary-sampling-param"] }
                pulse.default.frag      = { params_list["pulse-default-frag"] }/{ params_list["arbitrary-sampling-param"] }
                pulse.default.tlength   = { params_list["pulse-default-tlength"] }/{ params_list["arbitrary-sampling-param"] }
                pulse.min.quantum       = { params_list["pulse-min-quantum"] }/{ params_list["arbitrary-sampling-param"] }
                pulse.idle.timeout      = { params_list["pulse-idle-timeout"] }
                pulse.default.format    = { params_list["pulse-default-format"] }
                pulse.default.position  = { params_list["pulse-default-position"] }
        }}
        """
        return template


def CreateConfigFilePipeWireJack(params_list:dict):
        template = f"""
        jack.properties = {{
                node.latency    = { params_list["node.latency"] }/{ params_list["arbitrary-sampling-param"] }
                node.rate       = { params_list["node.rate"] }/{ params_list["arbitrary-sampling-param"] }
                node.lock-quantum  = { params_list["node.lock-quantum"] }
                node.force-quantum = { params_list["node.force-quantum"] }
                jack.show-monitor  = { params_list["jack.show-monitor"] }
                jack.merge-monitor = { params_list["jack.merge-monitor"] }
                jack.show-midi     = { params_list["jack.show-midi"] }
                jack.short-name    = { params_list["jack.short-name"] }
                jack.filter-name   = { params_list["jack.filter-name"] }
                jack.filter-char   = { params_list["jack.filter-char"] }
                jack.self-connect-mode  = { params_list["jack.self-connect-mode"] }
                jack.locked-process     = { params_list["jack.locked-process"] }
                jack.default-as-system  = { params_list["jack.default-as-system"] }
                jack.fix-midi-events    = { params_list["jack.fix-midi-events"] }
                jack.global-buffer-size = { params_list["jack.global-buffer-size"] }
                jack.max-client-ports   = { params_list["jack.max-client-ports"] }
                jack.fill-aliases       = { params_list["jack.fill-aliases"] }
                jack.writable-input     = { params_list["jack.writable-input"] }
        }}
        """
        return template

def CreateConfigFilePipeWireClients(params_list:dict):
        template = f"""
        stream.properties = {{
                node.latency          = { params_list['node.latency']}
                node.autoconnect      = { params_list['node.autoconnect']}
                resample.quality      = { params_list['resample.quality']}
                channelmix.normalize  = { params_list['channelmix.normalize']}
                channelmix.mix-lfe    = { params_list['channelmix.mix-lfe']}
                channelmix.upmix      = { params_list['channelmix.upmix']}
                channelmix.upmix-method = { params_list['channelmix.upmix-method']}
                channelmix.lfe-cutoff = { params_list['channelmix.lfe-cutoff']}
                channelmix.fc-cutoff  = { params_list['channelmix.fc-cutoff']}
                channelmix.rear-delay = { params_list['channelmix.rear-delay']}
                channelmix.stereo-widen = { params_list['channelmix.stereo-widen']}
                channelmix.hilbert-taps = { params_list['channelmix.hilbert-taps']}
                dither.noise = { params_list['dither.noise']}
        }}

        
        alsa.properties = {{
                alsa.deny = {params_list['alsa.deny']}
                alsa.format = [ {params_list['alsa.format']} ]
                alsa.rate = {{ {params_list['alsa.rate']} }}
                alsa.channels = {{ {params_list['alsa.channels']} }}
                alsa.period-bytes = {{ {params_list['alsa.period-bytes']} }}
                alsa.buffer-bytes = {{ {params_list['alsa.buffer-bytes']} }}
                alsa.volume-method = {params_list['alsa.volume-method']}
        }}

        """
        return template




        #os.path.isfile( home_path + '/.config/pipewire/pipewire-pulse.conf')
        #os.path.isfile( home_path + '/.config/pipewire/pipewire-avb.conf')
        #os.path.isfile( home_path + '/.config/pipewire/jack.conf')
        #os.path.isfile( home_path + '/.config/pipewire/filter-chain.conf')
        #os.path.isfile( home_path + '/.config/pipewire/client.conf')
        #os.path.isfile( home_path + '/.config/pipewire/client-rt.conf')
        #wireplumber configs
        #self.ConfigurationFileExits( home_path + '/.config/wireplumber/main.lua.d/50-alsa-config.lua')
        #self.ConfigurationFileExits( home_path + '/.config/wireplumber/main.lua.d/99-stop-microphone-auto-adjust.lua')
        #self.ConfigurationFileExits( home_path + '/.config/wireplumber/main.lua.d/100-custom-overwrites.lua')