
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