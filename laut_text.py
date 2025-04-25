def init_localization():
    global pwmain_tooltip_text
    pwmain_tooltip_text = """Main Pipewire settings most applications should use this settings by default, but some specific may use other audio subserver"""    
    global sample_rate_tooltip_text
    sample_rate_tooltip_text = "Default Sample Rate to which all audio streams will try to conform"
    global sample_tooltip_text
    sample_tooltip_text = """Sample Rate is equivalent of a resolution for audio."""
    global allowed_sample_tooltip_text
    allowed_sample_tooltip_text = "Allowed Sample Rates, defines which sample rates can be requested by a programs that run natively on a different rate"
    global quantum_tooltip_text
    quantum_tooltip_text = """Quantum is a period for which audio is going to be buffered.
In case of any crackling or stuttering of audio quantum minium value should be increased."""
    global quantum_def_text
    quantum_def_text = """Quantum will be set to this value at the start,it will adjust afterwards, in most cases going down to the minimum value set"""
    global quantum_min_text
    quantum_min_text = """This is soft limit, bellow which quantum wont be decreased"""
    global quantum_max_text
    quantum_max_text = """This is soft limit, above which quantum wont be increased"""
    global quantum_flor_text
    quantum_flor_text = """This is hard limit, above which quantum wont be decreased""" 
    global quantum_limit_text
    quantum_limit_text = """This is hard limit, above which quantum wont be increased"""

    global resampling_quality
    resampling_quality = """If audio stream is 
both up-sampling and down-sampling will affect quality of audio played """

    global save_button_tooltip
    save_button_tooltip = "Current configuration will be saved to your home folder .config folder"
    global reload_button_tooltip
    reload_button_tooltip = "This will reload last saved version of configuration"
    global apply_button_tooltip
    apply_button_tooltip = "This will reset wireplumber, pipewire and pipewire-pulse"
    global main_header_pulse_txt
    main_header_pulse_txt = "Pipewire-Pulse Settings:"
    global main_header_pipewire_txt
    main_header_pipewire_txt = "Pipewire Settings:"
    global main_header_jack_txt
    main_header_jack_txt = "Pipewire-Jack Settings:"
    global main_header_clients_txt
    main_header_clients_txt = "Alsa Clients Settings:"
    global link_buffers_max_tooltip
    link_buffers_max_tooltip = """The maximum number of buffers to negotiate between nodes.
More buffers is almost always worse, increasing latency and memory usage. So increase it only if you have to"""
    global pipewire_version_panel_header
    pipewire_version_panel_header = "Information about Pipewire Version"
    global version_disclamer
    version_disclamer = "Note: most up to date version might not be included within your system distribution"
    global version_current
    version_current = "Current Version:"
    global version_newest
    version_newest = "Newest Version"
    global pulse_sample_rate_tooltip_text
    pulse_sample_rate_tooltip_text = "Default Sample Rate to which all pulseaudio streams will try to conform"
    global pulse_nodes_latency_tooltip_text
    pulse_nodes_latency_tooltip_text = "Suggested latency for nodes"
    global pulse_resampling_quality_tooltip_text
    pulse_resampling_quality_tooltip_text = """Quality of resampling, higher values are better quality but will increase cpu usage
Middle values 4 to 6 are suggested:
    -4 gives best performance without any audio artifacts 
    -6 is best quality with not that much performance impact"""
    global pulse_req_min_tooltip_text
    pulse_req_min_tooltip_text = """Minimum data requested for client,
lowering this value and total length will decrease latency, but will increase CPU overhead"""
    global pulse_req_def_tooltip_text
    pulse_req_def_tooltip_text = """Default data requested for client,
if theres no specified value by client then this one will be used."""
    global pulse_frag_min_tooltip_text
    pulse_frag_min_tooltip_text = "Minimum size of capture buffer before it's send to a client"
    global pulse_frag_def_tooltip_text
    pulse_frag_def_tooltip_text = "Default size of capture buffer before it's send to a client"
    global pulse_tlen_tooltip_text
    pulse_tlen_tooltip_text = """Total data length which will be buffered on server side,
Lower values will decrease latency"""
    global pulse_pulsequantummin_tooltip_text
    pulse_pulsequantummin_tooltip_text = "Minimum quantum value, quantum value is based on ratio of requested data to total length of data"
    global pulse_def_format_tooltip_text
    pulse_def_format_tooltip_text = "Audio will default to this format if there's no specific one requested"
    global pulse_def_position_tooltip_text
    pulse_def_position_tooltip_text = "Default audio channels position"
    global pulse_idle_timeout_tooltip_text    
    pulse_idle_timeout_tooltip_text = "Disables clients that are idling for given amount of seconds, if set to 0 then its disabled"


    global label_sample_rate
    label_sample_rate = "Sample Rate:"
    global label_nodes_latency_tooltip_text
    label_nodes_latency_tooltip_text = "Nodes Latency:"
    global label_resampling_quality_tooltip_text
    label_resampling_quality_tooltip_text = "Resampling Quality:"
    global label_req_min_tooltip_text
    label_req_min_tooltip_text = "Request Min:"
    global label_req_def_tooltip_text
    label_req_def_tooltip_text = "Request Default:"
    global label_frag_min_tooltip_text
    label_frag_min_tooltip_text = "Fragmentation Min:"
    global label_frag_def_tooltip_text
    label_frag_def_tooltip_text = "Fragmentation Default:"
    global label_tlen_tooltip_text
    label_tlen_tooltip_text = "Total Length:"
    global label_pulsequantummin_tooltip_text
    label_pulsequantummin_tooltip_text = "Quantum Minimum:"
    global label_def_format_tooltip_text
    label_def_format_tooltip_text = "Default Format:"
    global label_def_position_tooltip_text
    label_def_position_tooltip_text = "Default Position:"
    global label_idle_timeout_tooltip_text
    label_idle_timeout_tooltip_text = "Idle Timeout:"
    global label_pulse_samples_header
    label_pulse_samples_header = "Pulse Sampling:"
    global label_stream_props
    label_stream_props = "Stream Properties:"
    global label_buffer_settings
    label_buffer_settings = "Buffer Settings:"
    global label_pulse_other_settings
    label_pulse_other_settings = "Other Settings:"

    global pulse_samples_header_tooltip
    pulse_samples_header_tooltip = "Sample Rate is equivalent of a resolution for audio."
    global stream_props_tooltip
    stream_props_tooltip = "Those properties apply to client streams for pulseaudio"
    global buffer_settings_tooltip
    buffer_settings_tooltip = "Various buffering settings"
    global pulse_other_settings_tooltip
    pulse_other_settings_tooltip = "More specific settings"

# Jack
    global label_Jack_samples_header
    label_Jack_samples_header = "Jack Sampling:"
    global Jack_samples_header_tooltip
    Jack_samples_header_tooltip = "Samples can be treated as an euqivalent to resolution"
    global Jack_sample_rate_tooltip_text
    Jack_sample_rate_tooltip_text = ""
    global label_jack_placeholder
    label_jack_placeholder = "placeholder"
    global jack_placeholder_tooltip_text
    jack_placeholder_tooltip_text = ""

    global jack_tooltip_text_JackNodeLockQuantum
    jack_tooltip_text_JackNodeLockQuantum ="Enforces default quantum on all Jack applications"
    global jack_tooltip_text_JackNodeForceQuantum
    jack_tooltip_text_JackNodeForceQuantum ="Will force specific value of quantum on all applications overrides lock quantum setting"
    global jack_tooltip_text_JackshowMonitor
    jack_tooltip_text_JackshowMonitor ="Shows monitor client and its ports"
    global jack_tooltip_text_JackmergeMonitor
    jack_tooltip_text_JackmergeMonitor ="Exposes capture and monitor ports on the same Jack device client"
    global jack_tooltip_text_JackshowMidi
    jack_tooltip_text_JackshowMidi ="Shows MIDI client and its ports"
    global jack_tooltip_text_JackshortName
    jack_tooltip_text_JackshortName ="Will use shorter names for ports and clients"
    global jack_tooltip_text_JackfilterName
    jack_tooltip_text_JackfilterName ="Enables char filter"
    global jack_tooltip_text_JackfilterChar
    jack_tooltip_text_JackfilterChar ="Replaces special characters for clients with specifed characters"
    global jack_tooltip_text_JackselfConnect
    jack_tooltip_text_JackselfConnect ="Specifies whether and what types of self connection are allowed"
    global jack_tooltip_text_JacklockedProcess
    jack_tooltip_text_JacklockedProcess ="Makes sure the process and callbacks can not be called at the same time"
    global jack_tooltip_text_JackdefaultAs
    jack_tooltip_text_JackdefaultAs ="Defaults name of outputs and inputs to \"System:\""
    global jack_tooltip_text_JackfixMidiEvents
    jack_tooltip_text_JackfixMidiEvents ="Mutes Midi Notes that are bellow or equal to 0 treshold"
    global jack_tooltip_text_JackglobalBufferSize
    jack_tooltip_text_JackglobalBufferSize ="Applies buffer size to all pipewire JACK clients"
    global jack_tooltip_text_JackmaxClientPorts
    jack_tooltip_text_JackmaxClientPorts ="Makes JACK clients make passive links." \
    "This option only works when the server link-factory was configured with the allow.link.passive option."
    global jack_tooltip_text_JackfillAliases
    jack_tooltip_text_JackfillAliases ="Automatically set the port alias1 and alias2 on the ports."
    global jack_tooltip_text_JackwritableInput   
    jack_tooltip_text_JackwritableInput    ="Makes the input buffers writable."
    global jack_tooltip_text_JackNodeLatency
    jack_tooltip_text_JackNodeLatency ="Allows setting a specific lattency for JACK clients"
    global label_Jack_Settings_header
    label_Jack_Settings_header ="Jack Settings"
    global Jack_Settings_header_tooltip
    Jack_Settings_header_tooltip ="Various JACK specific properties"    
    global jack_tooltip_text_JackNodeQuantum 
    jack_tooltip_text_JackNodeQuantum  =" "
    global label_jack_JackNodeLockQuantum
    label_jack_JackNodeLockQuantum ="Lock Quantum"
    global label_jack_JackNodeForceQuantum
    label_jack_JackNodeForceQuantum ="Force Quantum"
    global label_jack_JackshowMonitor
    label_jack_JackshowMonitor ="Show Monitor"
    global label_jack_JackmergeMonitor
    label_jack_JackmergeMonitor ="Merge Monitor"
    global label_jack_JackshowMidi
    label_jack_JackshowMidi ="Show MIDI"
    global label_jack_JackshortName
    label_jack_JackshortName ="Shorten Names"
    global label_jack_JackfilterName
    label_jack_JackfilterName ="Enable Filtering"
    global label_jack_JackfilterChar
    label_jack_JackfilterChar ="Filter Special Chars With"
    global label_jack_JackselfConnect
    label_jack_JackselfConnect ="Self Connection Options"
    global label_jack_JacklockedProcess
    label_jack_JacklockedProcess ="Lock Process"
    global label_jack_JackdefaultAs
    label_jack_JackdefaultAs ="System As Default"
    global label_jack_JackfixMidiEvents
    label_jack_JackfixMidiEvents ="Fix MIDI Events"
    global label_jack_JackglobalBufferSize
    label_jack_JackglobalBufferSize ="Set Global Buffer Size"
    global label_jack_JackmaxClientPorts
    label_jack_JackmaxClientPorts ="Max Clients Limit"
    global label_jack_JackfillAliases
    label_jack_JackfillAliases ="Fill Aliases"
    global label_jack_JackwritableInput
    label_jack_JackwritableInput ="Writable Input"
    global label_jack_JackNodeLatency
    label_jack_JackNodeLatency ="Nodes Latency"
    global label_jack_JackNodeRate
    label_jack_JackNodeRate ="Nodes Rate"
    global label_jack_JackNodeQuantum
    label_jack_JackNodeQuantum ="Node Quantum"
#clients
    global label_SampleRateLoadedClients
    label_SampleRateLoadedClients = "Samples"
    global label_ClientsNodeLatency
    label_ClientsNodeLatency = "Nodes Latency"
    global label_ClientsResampleQuality
    label_ClientsResampleQuality = "Resampling Quality"
    global label_ClientsNodeAutoconnect
    label_ClientsNodeAutoconnect = "Node Autoconnect"
    global label_ClientsChannelmixNormalize
    label_ClientsChannelmixNormalize = "Normalize Channels"
    global label_ClientsChannelmixMixlfe
    label_ClientsChannelmixMixlfe = "Channel Mix LFE"
    global label_ClientsChannelmixUpmix
    label_ClientsChannelmixUpmix = "Channel Upmix"
    global label_ClientsChannelmixUpmixMethod
    label_ClientsChannelmixUpmixMethod = "Channels Upmix Method"
    global label_ClientsChannelmixLfecutoff
    label_ClientsChannelmixLfecutoff = "Channels LFE Cutoff"
    global label_ClientsChannelmixFccutoff
    label_ClientsChannelmixFccutoff = "Channels FC Cuftoff"
    global label_ClientsChannelmixReardelay
    label_ClientsChannelmixReardelay = "Channel Mix Rear Dealay"
    global label_ClientsChannelmixStereowiden
    label_ClientsChannelmixStereowiden = "Channel Widen Stereo"
    global label_ClientsChannelmixHilberttaps
    label_ClientsChannelmixHilberttaps = "Channel Mix Hiblert taps"
    global label_ClientsDitherNoise
    label_ClientsDitherNoise = "Dither Noise"
    global clients_tooltip_text_SampleRateLoadedClients
    clients_tooltip_text_SampleRateLoadedClients = "Sample Rate is equivalent of a resolution for audio."
    global clients_tooltip_text_ClientsNodeLatency
    clients_tooltip_text_ClientsNodeLatency = """Sets a suggested latency this value works sames as Quantum
    (technically latency is quantum value/sample rate)"""
    global clients_tooltip_text_ClientsResampleQuality
    clients_tooltip_text_ClientsResampleQuality = """Quality of resampling, higher values are better quality but will increase cpu usage
Middle values 4 to 6 are suggested:
    -4 gives best performance without any audio artifacts 
    -6 is best quality with not that much performance impact"""
    global clients_tooltip_text_ClientsNodeAutoconnect
    clients_tooltip_text_ClientsNodeAutoconnect = "Should nodes be automatically connected to a sink or source"
    global clients_tooltip_text_ClientsChannelmixNormalize
    clients_tooltip_text_ClientsChannelmixNormalize = "Makes sure that during such mixing & resampling original 0 dB level is preserved, so nothing sounds wildly quieter/louder."
    global clients_tooltip_text_ClientsChannelmixMixlfe
    clients_tooltip_text_ClientsChannelmixMixlfe = """Mixes the low frequency effect channel into the front center or stereo pair. 
This might enhance the dynamic range of the signal if there is no subwoofer and the speakers can reproduce the low frequency signal."""
    global clients_tooltip_text_ClientsChannelmixUpmix
    clients_tooltip_text_ClientsChannelmixUpmix = """Enables up-mixing of the front center (FC) when the target has a FC channel. " \
    The sum of the stereo channels is used and an optional lowpass filter can be used (see channelmix.fc-cutoff)."""
    global clients_tooltip_text_ClientsChannelmixUpmixMethod
    clients_tooltip_text_ClientsChannelmixUpmixMethod = """
    none. No rear channels are produced.
    simple. Front channels are copied to the rear. This is fast but can produce phasing effects.
    psd. The rear channels as produced from the front left and right ambient sound (the difference between the channels). A delay and optional phase shift are added to the rear signal to make the sound bigger.
"""
    global clients_tooltip_text_ClientsChannelmixLfecutoff
    clients_tooltip_text_ClientsChannelmixLfecutoff = "Apply a lowpass filter to the low frequency effects. The value is expressed in Hz. Typical subwoofers have a cutoff at around 150 and 200. Value of 0 disables the feature."
    global clients_tooltip_text_ClientsChannelmixFccutoff
    clients_tooltip_text_ClientsChannelmixFccutoff = "Apply a lowpass filter to the front center frequency. The value is expressed in Hz. This option is only active when the up-mix is enabled. "
    global clients_tooltip_text_ClientsChannelmixReardelay
    clients_tooltip_text_ClientsChannelmixReardelay = "Apply a delay in milliseconds when up-mixing the rear channels. This is only active when the psd up-mix method is used."
    global clients_tooltip_text_ClientsChannelmixStereowiden
    clients_tooltip_text_ClientsChannelmixStereowiden = "Subtracts some of the front center signal from the stereo channels. This moves the dialogs more to the center speaker and leaves the ambient sound in the stereo channels."
    global clients_tooltip_text_ClientsChannelmixHilberttaps
    clients_tooltip_text_ClientsChannelmixHilberttaps = "This option will apply a 90 degree phase shift to the rear channels to improve specialization. Taps needs to be between 15 and 255 with more accurate results. This is only active when the psd up-mix method is used."
    global clients_tooltip_text_ClientsDitherNoise    
    clients_tooltip_text_ClientsDitherNoise = "Applies random noise over audio ranges from 0 to 1024 samples"

    global clients_tooltip_text_ClientsAlsaDeny
    clients_tooltip_text_ClientsAlsaDeny = "Denies ALSA access for the client"
    global clients_tooltip_text_ClientsAlsaAccess
    clients_tooltip_text_ClientsAlsaAccess = ""
    global clients_tooltip_text_ClientsAlsaFormat
    clients_tooltip_text_ClientsAlsaFormat = "The ALSA format to use for the client. 0 allows all formats"
    global clients_tooltip_text_ClientsAlsaRate
    clients_tooltip_text_ClientsAlsaRate = "The samplerate to use for the client. The default is 0, which is to allow all rates."
    global clients_tooltip_text_ClientsAlsaChannels
    clients_tooltip_text_ClientsAlsaChannels = "The number of channels for the client. The default is 0, which is to allow any number of channels."
    global clients_tooltip_text_ClientsAlsaPeriodbytes
    clients_tooltip_text_ClientsAlsaPeriodbytes = "The number of bytes per period. The default is 0 which is to allow any number of period bytes."
    global clients_tooltip_text_ClientsAlsaBufferbytes
    clients_tooltip_text_ClientsAlsaBufferbytes = "The number of bytes in the alsa buffer. The default is 0, which is to allow any number of bytes."
    global clients_tooltip_text_ClientsAlsaVolumeMethod
    clients_tooltip_text_ClientsAlsaVolumeMethod = "This controls the volume curve used on the ALSA mixer. Possible values are cubic and linear. The default is to use cubic."
    global label_ClientsAlsaDeny
    label_ClientsAlsaDeny = "Deny Access"
    global label_ClientsAlsaAccess
    label_ClientsAlsaAccess = "ALSA Access"
    global label_ClientsAlsaFormat
    label_ClientsAlsaFormat = "ALSA Format"
    global label_ClientsAlsaRate
    label_ClientsAlsaRate = "ALSA Rate"
    global label_ClientsAlsaChannels
    label_ClientsAlsaChannels = "ALSA Channels"
    global label_ClientsAlsaPeriodbytes
    label_ClientsAlsaPeriodbytes = "ALSA Period Bytes"
    global label_ClientsAlsaBufferbytes
    label_ClientsAlsaBufferbytes = "ALSA Buffer Bytes"
    global label_ClientsAlsaVolumeMethod
    label_ClientsAlsaVolumeMethod = "ALSA Volume Method"
    #headers
    global label_Clients_samples_header
    label_Clients_samples_header = "Clients Samples:"
    global label_Clients_samples_header_tooltip
    label_Clients_samples_header_tooltip = ""
    global label_Clients_various_header
    label_Clients_various_header = "Clients Other:"
    global label_Clients_various_header_tooltip
    label_Clients_various_header_tooltip = ""
    global label_Alsa_various_header
    label_Alsa_various_header = "ALSA Settings"
    global label_Alsa_various_header_tooltip
    label_Alsa_various_header_tooltip = ""