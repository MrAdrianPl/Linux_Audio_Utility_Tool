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
    version_disclamer = "Note that most up to date version might not be included within your system distribution"
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