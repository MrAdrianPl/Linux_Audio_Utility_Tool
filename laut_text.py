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
In case of any crackling or stuttering of audio quantum minmum value should be increased."""
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
both upsampling and downsampling will affect quality of audio played """

    global save_button_tooltip
    save_button_tooltip = "Curent configuration will be saved to your home folder .config folder"
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
    pipewire_version_panel_header = "Informations about Pipewire Version"
    global version_disclamer
    version_disclamer = "Note that most up to date version might not be included within your system distribution"
    global version_current
    version_current = "Current Version:"
    global version_newest
    version_newest = "Newest Version"