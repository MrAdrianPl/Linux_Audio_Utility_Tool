import sys
import os
from PyQt6.QtCore import QSize,Qt
from PyQt6.QtWidgets import (QApplication
                             ,QMainWindow
                             ,QPlainTextEdit
                             ,QVBoxLayout
                             ,QHBoxLayout
                             ,QWidget
                             ,QLabel
                             ,QTabWidget
                             ,QGridLayout
                             ,QSizePolicy
                             ,QScrollArea
                             )
from laut_gui_templates import (warning_icon
                                ,StandardDropdownTemplate
                                ,StandardCheckboxTemplate
                                ,StandardInputTemplate
                                ,StandardLableTemplate
                                ,StandardButtonTemplate
                                ,info_icon
                                ,AbsLableTemplate)
from laut_functions import (GetPWVersion
                            ,GetDevicesBasicInfo
                            ,GetDeviceCurrentProperties
                            ,GetConfigurationPath
                            ,ConfigExitsCheck
                            ,RestartPWServices
                            ,subConfigExitsCheck
                            ,GetMostUpToDateVersion
                            ,my_coalesce
                            ,RemoveOverrideProperties
                            ,ParsePropertiesIntoDict
                            ,strtobool)
from laut_files_handling import LoadPwJson,CreateConfigFilePipeWire,CreateConfigFilePipeWirePulse,CreateConfigFilePipeWireJack,CreateConfigFilePipeWireClients
import laut_text
import laut_events

class MainWindow(QMainWindow):

    ### Build Itself ###
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Linux Audio Utility Tools")

        self.resize(1920, 1080)

        tabs = self.Tab_Headers()

        mainl = QVBoxLayout()
        w = QWidget()
        mainl.addWidget(tabs)
        w.setLayout(mainl)

        self.setCentralWidget(w)

    ### Tabs ###

    def Tab_Headers(self):
        tabs = QTabWidget()
        tabs.setTabPosition(QTabWidget.TabPosition.North)
        #tabs.addTab(self.All_Outputs_Tab(),"Outputs Info")
        tabs.addTab(self.Pipewire_Configuration_Tab(),"Pipewire Configuration")
        #Devices info
        tabs.addTab(self.All_Devices_Tab(),"Devices Info")
        #Advanced
        #tabs.addTab(self.All_Outputs_Tab(),"Application Overrides")
        #tabs.addTab(self.All_Outputs_Tab(),"Virtual Ouptu/Input Devices")
        #tabs.addTab(self.Alsa_Configuration_Tab(),"Alsa Device Settings")
        tabs.setProperty("class","tabs_class")

        return tabs


    def All_Devices_Tab(self):


        minl = self.devices_panel()

        All_Devices_Tab_window = QWidget()
        All_Devices_Tab_window.setLayout(minl)
        return All_Devices_Tab_window

    def Pipewire_Configuration_Tab(self):
        laut_text.init_localization()

        tabsl = QTabWidget()
        tabsl.setTabPosition(QTabWidget.TabPosition.West)
        tabsl.addTab(self.pipewire_pulse_panel(),"Pipewire Pulse Settings")
        tabsl.addTab(self.pipewire_settings_panel_pw(),"Pipewire Settings")
        tabsl.addTab(self.pipewire_jack_panel(),"Pipewire Jack Settings")
        tabsl.addTab(self.pipewire_alsa_panel(),"Pipewire Clients Settings")

        minl = QGridLayout()
        topl = QHBoxLayout()
        midl = QHBoxLayout()
        # midls = self.pipewire_settings_panel_pw()
        # midld = self.pipewire_jack_panel()
        # midlt = self.pipewire_alsa_panel()
        bottml = QHBoxLayout()

        topl.addLayout(self.menu_buttons())
        bottml.addLayout(self.submenu_version_display())
        #verticalSpacer = QtWidgets.QSpacerItem(40, 20,  QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding) grid.addItem(verticalSpacer, 6, 0, QtCore.Qt.AlignTop)

        tabsl.setMaximumSize(1200,800)
        tabsl.setSizePolicy(QSizePolicy.Policy.Expanding,QSizePolicy.Policy.Expanding)
        midl.addWidget(tabsl)



        minl.addLayout(topl,0,0,Qt.AlignmentFlag.AlignLeft)
        minl.addLayout(midl,1,0,Qt.AlignmentFlag.AlignTop)
        # minl.addLayout(midl,1,1,Qt.AlignmentFlag.AlignTop)
        # minl.addLayout(midld,1,2,Qt.AlignmentFlag.AlignTop)
        # minl.addLayout(midlt,1,3,Qt.AlignmentFlag.AlignTop)
        minl.addLayout(bottml,2,0,Qt.AlignmentFlag.AlignLeft)

        Pipewire_Configuration_Tab_win = QWidget()

        Pipewire_Configuration_Tab_win.setLayout(minl)
        #Pipewire_Configuration_Tab_win.setSizePolicy(QSizePolicy.Policy.Expanding,QSizePolicy.Policy.Expanding)



        return Pipewire_Configuration_Tab_win

    def Alsa_Configuration_Tab(self):

        minl = QHBoxLayout()

        Alsa_Configuration_Tab_win = QWidget()
        Alsa_Configuration_Tab_win.setLayout(minl)
        return Alsa_Configuration_Tab_win

    ### panels

    def pipewire_settings_panel_pw(self):

        pipewire_data = self.LoadConfigurationFromFile('pipewire.conf')
        if pipewire_data is None:
            pipewire_data = {}

        ###get Config Values###
        SampleRateLoaded = pipewire_data['default.clock.rate'] if pipewire_data.get('default.clock.rate') is not None else "48000"
        AllowedRatesLoaded = pipewire_data['default.clock.allowed-rates'] if pipewire_data.get('default.clock.allowed-rates') is not None else "[ 44100 48000 88200 96000 176400 192000 352800 384000 ]"
        QuantumDefLoaded = pipewire_data['default.clock.quantum'] if pipewire_data.get('default.clock.quantum') is not None else "1024"
        QuantumMinLoaded = pipewire_data['default.clock.min-quantum'] if pipewire_data.get('default.clock.min-quantum') is not None else "512"
        QuandumMaxLoaded = pipewire_data['default.clock.max-quantum'] if pipewire_data.get('default.clock.max-quantum') is not None else "2048"
        QuantumLimitLoaded = pipewire_data['default.clock.quantum-limit'] if pipewire_data.get('default.clock.quantum-limit') is not None else "8192"
        LinkBuffersLoaded = pipewire_data['link.max-buffers'] if pipewire_data.get('link.max-buffers') is not None else "16"




        main_header_pw = StandardLableTemplate(laut_text.main_header_pipewire_txt,QSize(200, 40))
        main_header_pw.setProperty("class","Settings_Header")

        Main_Layout = QVBoxLayout()
        main_header_pw.setToolTip(laut_text.pwmain_tooltip_text)
        Main_Layout.addWidget(main_header_pw,alignment=Qt.AlignmentFlag.AlignTop)

        Button_space = QHBoxLayout()

        save_button = StandardButtonTemplate("Save Pipewire\nConfiguration",QSize(200, 40),self.SaveConfigurationForPipewire,laut_text.save_button_tooltip)
        Button_space.addWidget(save_button)

        Main_Layout.addLayout(Button_space)


        Lable_space = QHBoxLayout()



        Lable_space.addWidget(StandardLableTemplate("Sampling Settings:",QSize(120, 50)))
        Lable_space.addWidget(info_icon(36,36,laut_text.sample_tooltip_text),alignment=Qt.AlignmentFlag.AlignAbsolute)

        Main_Layout.addLayout(Lable_space)

        Main_Layout.addLayout(StandardDropdownTemplate('Sample Rate:',['16000','32000','44100','48000','88200','96000','176400','192000','352800','384000'],laut_events.SetSampleRateValue,str(SampleRateLoaded),laut_text.sample_rate_tooltip_text))
        Main_Layout.addLayout(StandardInputTemplate('Allowed Sampling Rates:',QSize(200, 28),laut_events.SetSampleAllowedRatesValue,str(AllowedRatesLoaded),laut_text.allowed_sample_tooltip_text))

        Lable_space_2 = QHBoxLayout()


        Lable_space_2.addWidget(StandardLableTemplate("Quantum Settings:",QSize(120, 50)))
        Lable_space_2.addWidget(info_icon(36,36,laut_text.quantum_tooltip_text),alignment=Qt.AlignmentFlag.AlignAbsolute)
        Main_Layout.addLayout(Lable_space_2)

        Main_Layout.addLayout(StandardDropdownTemplate('Quantum Def Rate:',['32','64','128','256','512','1024','2048','3072','4096','8192'],laut_events.SetQuantumDefValue,QuantumDefLoaded,laut_text.quantum_def_text))
        Main_Layout.addLayout(StandardDropdownTemplate('Quantum Min Rate:',['16','32','64','128','256','512','1024','2048','3072','4096'],laut_events.SetQuantumMinValue,QuantumMinLoaded,laut_text.quantum_min_text))
        Main_Layout.addLayout(StandardDropdownTemplate('Quantum Max Rate:',['256','512','1024','2048','3072','4096','8192','16384','32768'],laut_events.SetQuantumMaxValue,QuandumMaxLoaded,laut_text.quantum_max_text))
        Main_Layout.addLayout(StandardDropdownTemplate('Quantum Limit Rate:',['256','512','1024','2048','3072','4096','8192','16384','32768'],laut_events.SetQuantumLimitValue,QuantumLimitLoaded,laut_text.quantum_limit_text))
        #add warning icon with tooltip about quantums
        Main_Layout.addWidget(StandardLableTemplate("Other Settings:",QSize(120, 50)))
        Main_Layout.addLayout(StandardDropdownTemplate('Max Link Buffers:',['16','32','48','64'],laut_events.SetBuffersMaxLinkBuffers,LinkBuffersLoaded,laut_text.link_buffers_max_tooltip))
        main_header_pw.setAlignment(Qt.AlignmentFlag.AlignCenter)
        #link.max-buffers
        CurrentTab = QWidget()
        Main_Layout.setAlignment(Qt.AlignmentFlag.AlignTop)

        CurrentTab.setLayout(Main_Layout)
        ScrollArea = QScrollArea()
        ScrollArea.setWidget(CurrentTab)
        ScrollArea.setSizePolicy(QSizePolicy.Policy.Maximum,QSizePolicy.Policy.Expanding)
        ScrollArea.setWidgetResizable(True)

        return ScrollArea

    def pipewire_pulse_panel(self):
        #add warning icon with tooltip about above settings\

        pipewire_pulse_data = self.LoadConfigurationFromFile('pipewire-pulse.conf')
        if pipewire_pulse_data is None:
            pipewire_pulse_data = {}
        ###get Config Values###

        try:
            SampleRateLoadedPulse = (
                            my_coalesce(
                                    pipewire_pulse_data.get('pulse.min.req')
                                    ,pipewire_pulse_data.get('pulse.default.req')
                                    ,pipewire_pulse_data.get('pulse.min.frag')
                                    ,pipewire_pulse_data.get('pulse.default.frag')
                                    ,pipewire_pulse_data.get('pulse.default.tlength')
                                    ,pipewire_pulse_data.get('pulse.min.quantum')
                            )
                            )

            if SampleRateLoadedPulse is None:
                SampleRateLoadedPulse = "48000"
            else:
                SampleRateLoadedPulse = SampleRateLoadedPulse.split('/')[1]
        except IndexError:
            SampleRateLoadedPulse = "48000"
            print('Malformed Pipewire-Pulse Configuration')

        PulseRequestMin = pipewire_pulse_data.get('pulse.min.req').split('/')[0] if pipewire_pulse_data.get('pulse.min.req') is not None else "128"
        PulseRequestDef = pipewire_pulse_data.get('pulse.default.req').split('/')[0] if pipewire_pulse_data.get('pulse.default.req') is not None else "960"
        PulseFragMin = pipewire_pulse_data.get('pulse.min.frag').split('/')[0] if pipewire_pulse_data.get('pulse.min.frag') is not None else "128"
        PulseFragDef = pipewire_pulse_data.get('pulse.default.frag').split('/')[0] if pipewire_pulse_data.get('pulse.default.frag') is not None else "96000"
        PulseTLenDef = pipewire_pulse_data.get('pulse.default.tlength').split('/')[0] if pipewire_pulse_data.get('pulse.default.tlength') is not None else "96000"
        PulseQuantumMin = pipewire_pulse_data.get('pulse.min.quantum').split('/')[0] if pipewire_pulse_data.get('pulse.min.quantum') is not None else "128"
        PulseNodesLatency = pipewire_pulse_data.get('node.latency').split('/')[0] if pipewire_pulse_data.get('node.latency') is not None else "1024"
        PulseResamplingQuality = pipewire_pulse_data.get('resample.quality') if pipewire_pulse_data.get('resample.quality') is not None else "6"
        PulseIdleTimeout = pipewire_pulse_data.get('pulse.idle.timeout') if pipewire_pulse_data.get('pulse.idle.timeout') is not None else "0"
        PulseDefFormat = pipewire_pulse_data.get('pulse.default.format') if pipewire_pulse_data.get('pulse.default.format') is not None else "F32"
        PulseDefPosition = pipewire_pulse_data.get('pulse.default.position') if pipewire_pulse_data.get('pulse.default.position') is not None else "[FL FR]"

        ###GUI###

        main_header_pulse = StandardLableTemplate(laut_text.main_header_pulse_txt,QSize(200, 40))
        main_header_pulse.setProperty("class","Settings_Header")
        Main_Layout = QVBoxLayout()
        Main_Layout.addWidget(main_header_pulse,alignment=Qt.AlignmentFlag.AlignTop)

        Button_space = QHBoxLayout()

        save_button = StandardButtonTemplate("Save Pipewire-Pulse\nConfiguration",QSize(200, 40),self.SaveConfigurationForPipewirePulse,laut_text.save_button_tooltip)
        Button_space.addWidget(save_button)

        Main_Layout.addLayout(Button_space)


        Lable_space = QHBoxLayout()

        Lable_space = QHBoxLayout()

        Lable_space.addWidget(StandardLableTemplate(laut_text.label_pulse_samples_header,QSize(120, 50)))
        Lable_space.addWidget(info_icon(36,36,laut_text.pulse_samples_header_tooltip),alignment=Qt.AlignmentFlag.AlignAbsolute)
        Main_Layout.addLayout(Lable_space)

        Main_Layout.addLayout(StandardDropdownTemplate(laut_text.label_sample_rate,['16000','32000','44100','48000','88200','96000','176400','192000','352800','384000'],laut_events.SetPulseSample,SampleRateLoadedPulse,laut_text.pulse_sample_rate_tooltip_text))

        Lable_space2 = QHBoxLayout()

        Lable_space2.addWidget(StandardLableTemplate(laut_text.label_stream_props,QSize(120, 50)))
        Lable_space2.addWidget(info_icon(36,36,laut_text.stream_props_tooltip),alignment=Qt.AlignmentFlag.AlignAbsolute)
        Main_Layout.addLayout(Lable_space2)

        Main_Layout.addLayout(StandardDropdownTemplate(laut_text.label_nodes_latency_tooltip_text,['64','128','256','512','1024','2048','4096','8192','16384'],laut_events.SetPulseNodesLatency,PulseNodesLatency,laut_text.pulse_nodes_latency_tooltip_text))
        Main_Layout.addLayout(StandardDropdownTemplate(laut_text.label_resampling_quality_tooltip_text,['1','2','3','4','5','6','7','8','9','10'],laut_events.SetPulseResamplingQuality,PulseResamplingQuality,laut_text.pulse_resampling_quality_tooltip_text))
        Lable_space3 = QHBoxLayout()

        Lable_space3.addWidget(StandardLableTemplate(laut_text.label_buffer_settings,QSize(120, 50)))
        Lable_space3.addWidget(info_icon(36,36,laut_text.buffer_settings_tooltip),alignment=Qt.AlignmentFlag.AlignAbsolute)
        Main_Layout.addLayout(Lable_space3)

        Main_Layout.addLayout(StandardDropdownTemplate(laut_text.label_req_min_tooltip_text,['64','128','256','512','1024','2048','4096','8192','16384'],laut_events.SetPulseFragMin,PulseRequestMin,laut_text.pulse_req_min_tooltip_text))
        Main_Layout.addLayout(StandardDropdownTemplate(laut_text.label_req_def_tooltip_text,['360','480','960','1440','1920','2520','7680','15360'],laut_events.SetPulseFragDef,PulseRequestDef,laut_text.pulse_req_def_tooltip_text))
        Main_Layout.addLayout(StandardDropdownTemplate(laut_text.label_frag_min_tooltip_text,['64','128','256','512','1024','2048','4096','8192','16384'],laut_events.SetPulseReqMin,PulseFragMin,laut_text.pulse_frag_min_tooltip_text))
        Main_Layout.addLayout(StandardDropdownTemplate(laut_text.label_frag_def_tooltip_text,['16000','32000','44100','48000','88200','96000','176400','192000','352800','384000'],laut_events.SetPulseReqDef,PulseFragDef,laut_text.pulse_frag_def_tooltip_text))
        Main_Layout.addLayout(StandardDropdownTemplate(laut_text.label_tlen_tooltip_text,['16000','32000','44100','48000','88200','96000','176400','192000','352800','384000'],laut_events.SetPulseQuantMin,PulseTLenDef,laut_text.pulse_tlen_tooltip_text))
        Main_Layout.addLayout(StandardDropdownTemplate(laut_text.label_pulsequantummin_tooltip_text,['64','128','256','512','1024','2048','4096','8192','16384'],laut_events.SetPulseTLen,PulseQuantumMin,laut_text.pulse_pulsequantummin_tooltip_text))
        Lable_space4 = QHBoxLayout()

        Lable_space4.addWidget(StandardLableTemplate(laut_text.label_pulse_other_settings,QSize(120, 50)))
        Lable_space4.addWidget(info_icon(36,36,laut_text.pulse_other_settings_tooltip),alignment=Qt.AlignmentFlag.AlignAbsolute)
        Main_Layout.addLayout(Lable_space4)

        Main_Layout.addLayout(StandardDropdownTemplate(laut_text.label_def_format_tooltip_text,['U8','S16','S16LE','S24','S24LE','F32','F32LE'],laut_events.SetPulseDefaultFormat,PulseDefFormat,laut_text.pulse_def_format_tooltip_text))
        Main_Layout.addLayout(StandardInputTemplate(laut_text.label_def_position_tooltip_text,QSize(84, 28),laut_events.SetPulseDefaultPositon,PulseDefPosition,laut_text.pulse_def_position_tooltip_text))
        Main_Layout.addLayout(StandardInputTemplate(laut_text.label_idle_timeout_tooltip_text,QSize(42, 28),laut_events.SetPulseIdleTimeout,PulseIdleTimeout,laut_text.pulse_idle_timeout_tooltip_text))

        Main_Layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        main_header_pulse.setAlignment(Qt.AlignmentFlag.AlignCenter)

        CurrentTab = QWidget()
        CurrentTab.setLayout(Main_Layout)
        ScrollArea = QScrollArea()
        ScrollArea.setWidget(CurrentTab)
        ScrollArea.setSizePolicy(QSizePolicy.Policy.Maximum,QSizePolicy.Policy.Expanding)
        ScrollArea.setWidgetResizable(True)

        return ScrollArea

    def pipewire_jack_panel(self):
        pipewire_jack_data = self.LoadConfigurationFromFile('jack.conf')
        if pipewire_jack_data is None:
            pipewire_jack_data = {}
        SampleRateLoadedJack = (
                            my_coalesce(
                                    pipewire_jack_data.get('node.latency')
                                    ,pipewire_jack_data.get('node.rate')
                                    ,pipewire_jack_data.get('node.quantum')
                                )
                            )

        try:
            if SampleRateLoadedJack is None:
                SampleRateLoadedJack = "48000"
            else:
                SampleRateLoadedJack = SampleRateLoadedJack.split('/')[1]
        except IndexError:
            SampleRateLoadedJack = "48000"
            print('Malformed Pipewire-Jack Configuration')

        JackNodeLatency = pipewire_jack_data.get('node.latency').split('/')[0] if pipewire_jack_data.get('node.latency') is not None else "1024"

        JackNodeLockQuantum = pipewire_jack_data.get('node.lock-quantum') if pipewire_jack_data.get('node.lock-quantum') is not None else "True"
        JackNodeForceQuantum = pipewire_jack_data.get('node.force-quantum') if pipewire_jack_data.get('node.force-quantum') is not None else "0"
        JackshowMonitor = pipewire_jack_data.get('jack.show-monitor') if pipewire_jack_data.get('jack.show-monitor') is not None else "True"
        JackmergeMonitor = pipewire_jack_data.get('jack.merge-monitor') if pipewire_jack_data.get('jack.merge-monitor') is not None else "True"
        JackshowMidi = pipewire_jack_data.get('jack.show-midi') if pipewire_jack_data.get('jack.show-midi') is not None else "True"
        JackshortName = pipewire_jack_data.get('jack.short-name') if pipewire_jack_data.get('jack.short-name') is not None else "False"
        JackfilterName = pipewire_jack_data.get('jack.filter-name') if pipewire_jack_data.get('jack.filter-name') is not None else "False"
        JackfilterChar = pipewire_jack_data.get('jack.filter-char') if pipewire_jack_data.get('jack.filter-char') is not None else "\" \""
        JackselfConnect = pipewire_jack_data.get('jack.self-connect-mode') if pipewire_jack_data.get('jack.self-connect-mode') is not None else "allow"
        JacklockedProcess = pipewire_jack_data.get('jack.locked-process') if pipewire_jack_data.get('jack.locked-process') is not None else "True"
        JackdefaultAs = pipewire_jack_data.get('jack.default-as-system') if pipewire_jack_data.get('jack.default-as-system') is not None else "False"
        JackfixMidiEvents = pipewire_jack_data.get('jack.fix-midi-events') if pipewire_jack_data.get('jack.fix-midi-events') is not None else "True"
        JackglobalBufferSize = pipewire_jack_data.get('jack.global-buffer-size') if pipewire_jack_data.get('jack.global-buffer-size') is not None else "False"
        JackmaxClientPorts = pipewire_jack_data.get('jack.max-client-ports') if pipewire_jack_data.get('jack.max-client-ports') is not None else "768"
        JackfillAliases = pipewire_jack_data.get('jack.fill-aliases') if pipewire_jack_data.get('jack.fill-aliases') is not None else "False"
        JackwritableInput = pipewire_jack_data.get('jack.writable-input') if pipewire_jack_data.get('jack.writable-input') is not None else "True"

        main_header_jack = StandardLableTemplate(laut_text.main_header_jack_txt,QSize(200, 40))
        main_header_jack.setProperty("class","Settings_Header")




        Main_Layout = QVBoxLayout()


        Main_Layout.addWidget(main_header_jack,alignment=Qt.AlignmentFlag.AlignTop)
        main_header_jack.setAlignment(Qt.AlignmentFlag.AlignCenter)



        Button_space = QHBoxLayout()

        save_button = StandardButtonTemplate("Save Pipewire-Jack\nConfiguration",QSize(200, 40),self.SaveConfigurationForPipewireJack,laut_text.save_button_tooltip)
        Button_space.addWidget(save_button)

        Main_Layout.addLayout(Button_space)

        Lable_space = QHBoxLayout()

        Lable_space.addWidget(StandardLableTemplate(laut_text.label_Jack_samples_header,QSize(120, 50)))
        Lable_space.addWidget(info_icon(36,36,laut_text.Jack_samples_header_tooltip),alignment=Qt.AlignmentFlag.AlignAbsolute)
        Main_Layout.addLayout(Lable_space)

        Main_Layout.addLayout(StandardDropdownTemplate(laut_text.label_sample_rate,['16000','32000','44100','48000','88200','96000','176400','192000','352800','384000'],laut_events.SetJackSample,SampleRateLoadedJack,laut_text.Jack_sample_rate_tooltip_text))

        Lable_space2 = QHBoxLayout()

        Lable_space2.addWidget(StandardLableTemplate(laut_text.label_Jack_Settings_header,QSize(120, 50)))
        Lable_space2.addWidget(info_icon(36,36,laut_text.Jack_Settings_header_tooltip),alignment=Qt.AlignmentFlag.AlignAbsolute)
        Main_Layout.addLayout(Lable_space2)

        Main_Layout.addLayout(StandardDropdownTemplate(laut_text.label_jack_JackNodeLatency,['64','128','256','512','1024','2048','4096','8192','16384'],laut_events.SetJackNodeLatency,JackNodeLatency,laut_text.jack_tooltip_text_JackNodeLatency))

        Main_Layout.addLayout(StandardCheckboxTemplate(laut_text.label_jack_JackNodeLockQuantum,laut_events.SetJackNodeLockQuantum,strtobool(JackNodeLockQuantum),laut_text.jack_tooltip_text_JackNodeLockQuantum))
        Main_Layout.addLayout(StandardDropdownTemplate(laut_text.label_jack_JackNodeForceQuantum,['64','128','256','512','1024','2048','4096','8192','16384'],laut_events.SetJackNodeQuantum,JackNodeForceQuantum,laut_text.jack_tooltip_text_JackNodeQuantum))
        Main_Layout.addLayout(StandardCheckboxTemplate(laut_text.label_jack_JackshowMonitor,laut_events.SetJackshowMonitor,strtobool(JackshowMonitor),laut_text.jack_tooltip_text_JackshowMonitor))
        Main_Layout.addLayout(StandardCheckboxTemplate(laut_text.label_jack_JackmergeMonitor,laut_events.SetJackmergeMonitor,strtobool(JackmergeMonitor),laut_text.jack_tooltip_text_JackmergeMonitor))
        Main_Layout.addLayout(StandardCheckboxTemplate(laut_text.label_jack_JackshowMidi,laut_events.SetJackshowMidi,strtobool(JackshowMidi),laut_text.jack_tooltip_text_JackshowMidi))
        Main_Layout.addLayout(StandardCheckboxTemplate(laut_text.label_jack_JackshortName,laut_events.SetJackshortName,strtobool(JackshortName),laut_text.jack_tooltip_text_JackshortName))
        Main_Layout.addLayout(StandardCheckboxTemplate(laut_text.label_jack_JackfilterName,laut_events.SetJackfilterName,strtobool(JackfilterName),laut_text.jack_tooltip_text_JackfilterName))
        Main_Layout.addLayout(StandardInputTemplate(laut_text.label_jack_JackmaxClientPorts,QSize(84, 28),laut_events.SetJackfilterChar,JackfilterChar,laut_text.jack_tooltip_text_JackfilterChar))
        Main_Layout.addLayout(StandardDropdownTemplate(laut_text.label_jack_JackselfConnect,['allow','fail-external','ignore-external','fail-all','ignore-all'],laut_events.SetJackselfConnect,JackselfConnect,laut_text.jack_tooltip_text_JackselfConnect))
        Main_Layout.addLayout(StandardCheckboxTemplate(laut_text.label_jack_JacklockedProcess,laut_events.SetJacklockedProcess,strtobool(JacklockedProcess),laut_text.jack_tooltip_text_JacklockedProcess))
        Main_Layout.addLayout(StandardCheckboxTemplate(laut_text.label_jack_JackdefaultAs,laut_events.SetJackdefaultAs,strtobool(JackdefaultAs),laut_text.jack_tooltip_text_JackdefaultAs))
        Main_Layout.addLayout(StandardCheckboxTemplate(laut_text.label_jack_JackfixMidiEvents,laut_events.SetJackfixMidiEvents,strtobool(JackfixMidiEvents),laut_text.jack_tooltip_text_JackfixMidiEvents))
        Main_Layout.addLayout(StandardCheckboxTemplate(laut_text.label_jack_JackglobalBufferSize,laut_events.SetJackglobalBufferSize,strtobool(JackglobalBufferSize),laut_text.jack_tooltip_text_JackglobalBufferSize))
        Main_Layout.addLayout(StandardInputTemplate(laut_text.label_jack_JackmaxClientPorts,QSize(84, 28),laut_events.SetJackmaxClientPorts,JackmaxClientPorts,laut_text.jack_tooltip_text_JackmaxClientPorts))
        Main_Layout.addLayout(StandardCheckboxTemplate(laut_text.label_jack_JackfillAliases,laut_events.SetJackfillAliases,strtobool(JackfillAliases),laut_text.jack_tooltip_text_JackfillAliases))
        Main_Layout.addLayout(StandardCheckboxTemplate(laut_text.label_jack_JackwritableInput,laut_events.SetJackwritableInput,strtobool(JackwritableInput),laut_text.jack_tooltip_text_JackwritableInput))

        Main_Layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        CurrentTab = QWidget()
        CurrentTab.setLayout(Main_Layout)
        ScrollArea = QScrollArea()
        ScrollArea.setWidget(CurrentTab)
        ScrollArea.setSizePolicy(QSizePolicy.Policy.Maximum,QSizePolicy.Policy.Expanding)
        ScrollArea.setWidgetResizable(True)

        return ScrollArea

    def pipewire_alsa_panel(self):

        pipewire_clients_data = self.LoadConfigurationFromFile('client-rt.conf')
        if pipewire_clients_data is None:
            pipewire_clients_data = {}

        defSampleRateLoadedClients = pipewire_clients_data.get('node.latency')

        try:
            if defSampleRateLoadedClients is None:
                defSampleRateLoadedClients = "48000"
            else:
                defSampleRateLoadedClients = defSampleRateLoadedClients.split('/')[1]
        except IndexError:
            defSampleRateLoadedClients = "48000"
            print('Malformed Pipewire-clients-rt Configuration')

        main_header_alsa = StandardLableTemplate(laut_text.main_header_clients_txt,QSize(200, 40))
        main_header_alsa.setProperty("class","Settings_Header")
        Main_Layout = QVBoxLayout()
        Main_Layout.addWidget(main_header_alsa,alignment=Qt.AlignmentFlag.AlignTop)

        Button_space = QHBoxLayout()

        save_button = StandardButtonTemplate("Save Pipewire-Clients\nConfiguration",QSize(200, 40),self.SaveConfigurationForPipewireClients,laut_text.save_button_tooltip)
        Button_space.addWidget(save_button)

        Main_Layout.addLayout(Button_space)


        defClientsNodeLatency = pipewire_clients_data.get('node.latency').split('/')[0] if pipewire_clients_data.get('node.latency') is not None else "1024"
        defClientsNodeAutoconnect = pipewire_clients_data.get('node.autoconnect') if pipewire_clients_data.get('node.autoconnect') is not None else "true"
        defClientsResampleQuality = pipewire_clients_data.get('resample.quality') if pipewire_clients_data.get('resample.quality') is not None else "6"
        defClientsChannelmixNormalize = pipewire_clients_data.get('channelmix.normalize') if pipewire_clients_data.get('channelmix.normalize') is not None else "false"
        defClientsChannelmixMixlfe = pipewire_clients_data.get('channelmix.mix-lfe') if pipewire_clients_data.get('channelmix.mix-lfe') is not None else "true"
        defClientsChannelmixUpmix = pipewire_clients_data.get('channelmix.upmix') if pipewire_clients_data.get('channelmix.upmix') is not None else "true"
        defClientsChannelmixUpmixMethod = pipewire_clients_data.get('channelmix.upmix-method') if pipewire_clients_data.get('channelmix.upmix-method') is not None else "psd"
        defClientsChannelmixLfecutoff = pipewire_clients_data.get('channelmix.lfe-cutoff') if pipewire_clients_data.get('channelmix.lfe-cutoff') is not None else "150"
        defClientsChannelmixFccutoff = pipewire_clients_data.get('channelmix.fc-cutoff') if pipewire_clients_data.get('channelmix.fc-cutoff') is not None else "12000"
        defClientsChannelmixReardelay = pipewire_clients_data.get('channelmix.rear-delay') if pipewire_clients_data.get('channelmix.rear-delay') is not None else "12.0"
        defClientsChannelmixStereowiden = pipewire_clients_data.get('channelmix.stereo-widen') if pipewire_clients_data.get('channelmix.stereo-widen') is not None else "0.0"
        defClientsChannelmixHilberttaps = pipewire_clients_data.get('channelmix.hilbert-taps') if pipewire_clients_data.get('channelmix.hilbert-taps') is not None else "0"
        defClientsDitherNoise = pipewire_clients_data.get('dither.noise') if pipewire_clients_data.get('dither.noise') is not None else "0"


        Lable_space = QHBoxLayout()

        Lable_space.addWidget(StandardLableTemplate(laut_text.label_Clients_samples_header,QSize(120, 50)))
        Lable_space.addWidget(info_icon(36,36,laut_text.label_Clients_samples_header_tooltip),alignment=Qt.AlignmentFlag.AlignAbsolute)
        Main_Layout.addLayout(Lable_space)

        Main_Layout.addLayout(StandardDropdownTemplate(laut_text.label_SampleRateLoadedClients,['16000','32000','44100','48000','88200','96000','176400','192000','352800','384000'],laut_events.SetSampleRateLoadedClients,defSampleRateLoadedClients,laut_text.clients_tooltip_text_SampleRateLoadedClients))
        Main_Layout.addLayout(StandardDropdownTemplate(laut_text.label_ClientsNodeLatency,['64','128','256','512','1024','2048','4096','8192','16384'],laut_events.SetClientsNodeLatency,defClientsNodeLatency,laut_text.clients_tooltip_text_ClientsNodeLatency))
        Main_Layout.addLayout(StandardDropdownTemplate(laut_text.label_ClientsResampleQuality,['1','2','3','4','5','6','7','8','9','10'],laut_events.SetClientsResampleQuality,defClientsResampleQuality,laut_text.clients_tooltip_text_ClientsResampleQuality))

        Lable_space = QHBoxLayout()

        Lable_space.addWidget(StandardLableTemplate(laut_text.label_Clients_various_header,QSize(120, 50)))
        Lable_space.addWidget(info_icon(36,36,laut_text.label_Clients_various_header_tooltip),alignment=Qt.AlignmentFlag.AlignAbsolute)
        Main_Layout.addLayout(Lable_space)

        Main_Layout.addLayout(StandardCheckboxTemplate(laut_text.label_ClientsNodeAutoconnect,laut_events.SetClientsNodeAutoconnect,strtobool(defClientsNodeAutoconnect),laut_text.clients_tooltip_text_ClientsNodeAutoconnect))
        #mu
        Main_Layout.addLayout(StandardCheckboxTemplate(laut_text.label_ClientsChannelmixNormalize,laut_events.SetClientsChannelmixNormalize,strtobool(defClientsChannelmixNormalize),laut_text.clients_tooltip_text_ClientsChannelmixNormalize))
        Main_Layout.addLayout(StandardCheckboxTemplate(laut_text.label_ClientsChannelmixMixlfe,laut_events.SetClientsChannelmixMixlfe,strtobool(defClientsChannelmixMixlfe),laut_text.clients_tooltip_text_ClientsChannelmixMixlfe))
        Main_Layout.addLayout(StandardCheckboxTemplate(laut_text.label_ClientsChannelmixUpmix,laut_events.SetClientsChannelmixUpmix,strtobool(defClientsChannelmixUpmix),laut_text.clients_tooltip_text_ClientsChannelmixUpmix))

        Main_Layout.addLayout(StandardDropdownTemplate(laut_text.label_ClientsChannelmixUpmixMethod,['psd','none','simple'],laut_events.SetClientsChannelmixUpmixMethod,defClientsChannelmixUpmixMethod,laut_text.clients_tooltip_text_ClientsChannelmixUpmixMethod))
        Main_Layout.addLayout(StandardInputTemplate(laut_text.label_ClientsChannelmixLfecutoff,QSize(84, 28),laut_events.SetClientsChannelmixLfecutoff,defClientsChannelmixLfecutoff,laut_text.clients_tooltip_text_ClientsChannelmixLfecutoff))
        Main_Layout.addLayout(StandardInputTemplate(laut_text.label_ClientsChannelmixFccutoff,QSize(84, 28),laut_events.SetClientsChannelmixFccutoff,defClientsChannelmixFccutoff,laut_text.clients_tooltip_text_ClientsChannelmixFccutoff))
        Main_Layout.addLayout(StandardInputTemplate(laut_text.label_ClientsChannelmixReardelay,QSize(84, 28),laut_events.SetClientsChannelmixReardelay,defClientsChannelmixReardelay,laut_text.clients_tooltip_text_ClientsChannelmixReardelay))
        Main_Layout.addLayout(StandardInputTemplate(laut_text.label_ClientsChannelmixStereowiden,QSize(84, 28),laut_events.SetClientsChannelmixStereowiden,defClientsChannelmixStereowiden,laut_text.clients_tooltip_text_ClientsChannelmixStereowiden))
        Main_Layout.addLayout(StandardInputTemplate(laut_text.label_ClientsChannelmixHilberttaps,QSize(84, 28),laut_events.SetClientsChannelmixHilberttaps,defClientsChannelmixHilberttaps,laut_text.clients_tooltip_text_ClientsChannelmixHilberttaps))
        Main_Layout.addLayout(StandardInputTemplate(laut_text.label_ClientsDitherNoise,QSize(84, 28),laut_events.SetClientsDitherNoise,defClientsDitherNoise,laut_text.clients_tooltip_text_ClientsDitherNoise))

        Lable_space = QHBoxLayout()

        Lable_space.addWidget(StandardLableTemplate(laut_text.label_Alsa_various_header,QSize(120, 50)))
        Lable_space.addWidget(info_icon(36,36,laut_text.label_Alsa_various_header_tooltip),alignment=Qt.AlignmentFlag.AlignAbsolute)
        Main_Layout.addLayout(Lable_space)

        main_header_alsa.setAlignment(Qt.AlignmentFlag.AlignCenter)

        defClientsAlsaDeny = pipewire_clients_data.get('alsa.deny') if pipewire_clients_data.get('alsa.deny') is not None else "false"
        #defClientsAlsaAccess = pipewire_clients_data.get('alsa.access') if pipewire_clients_data.get('alsa.access') is not None else "[ MMAP_INTERLEAVED MMAP_NONINTERLEAVED RW_INTERLEAVED RW_NONINTERLEAVED ]"
        defClientsAlsaFormat = pipewire_clients_data.get('alsa.format') if pipewire_clients_data.get('alsa.format') is not None else "[ FLOAT S32 S24 S24_3 S16 U8 ]"
        defClientsAlsaRate = pipewire_clients_data.get('alsa.rate') if pipewire_clients_data.get('alsa.rate') is not None else "{ min=1 max=384000 }"
        defClientsAlsaChannels = pipewire_clients_data.get('alsa.channels') if pipewire_clients_data.get('alsa.channels') is not None else "{ min=1 max=64 }"
        defClientsAlsaPeriodbytes = pipewire_clients_data.get('alsa.period-bytes') if pipewire_clients_data.get('alsa.period-bytes') is not None else "{ min=128 max=2097152 }"
        defClientsAlsaBufferbytes = pipewire_clients_data.get('alsa.buffer-bytes') if pipewire_clients_data.get('alsa.buffer-bytes') is not None else "{ min=256 max=4194304 }"
        defClientsAlsaVolumeMethod = pipewire_clients_data.get('alsa.volume-method') if pipewire_clients_data.get('alsa.volume-method') is not None else "cubic"

        Main_Layout.addLayout(StandardCheckboxTemplate(laut_text.label_ClientsAlsaDeny,laut_events.SetClientsAlsaDeny,strtobool(defClientsAlsaDeny),laut_text.clients_tooltip_text_ClientsAlsaDeny))
        #Main_Layout.addLayout(StandardInputTemplate(laut_text.label_ClientsAlsaAccess,QSize(200, 28),laut_events.SetClientsAlsaAccess,defClientsAlsaAccess,laut_text.clients_tooltip_text_ClientsAlsaAccess))
        Main_Layout.addLayout(StandardInputTemplate(laut_text.label_ClientsAlsaFormat,QSize(200, 28),laut_events.SetClientsAlsaFormat,defClientsAlsaFormat,laut_text.clients_tooltip_text_ClientsAlsaFormat))
        Main_Layout.addLayout(StandardInputTemplate(laut_text.label_ClientsAlsaRate,QSize(128, 28),laut_events.SetClientsAlsaRate,defClientsAlsaRate,laut_text.clients_tooltip_text_ClientsAlsaRate))
        Main_Layout.addLayout(StandardInputTemplate(laut_text.label_ClientsAlsaChannels,QSize(128, 28),laut_events.SetClientsAlsaChannels,defClientsAlsaChannels,laut_text.clients_tooltip_text_ClientsAlsaChannels))
        Main_Layout.addLayout(StandardInputTemplate(laut_text.label_ClientsAlsaPeriodbytes,QSize(128, 28),laut_events.SetClientsAlsaPeriodbytes,defClientsAlsaPeriodbytes,laut_text.clients_tooltip_text_ClientsAlsaPeriodbytes))
        Main_Layout.addLayout(StandardInputTemplate(laut_text.label_ClientsAlsaBufferbytes,QSize(128, 28),laut_events.SetClientsAlsaBufferbytes,defClientsAlsaBufferbytes,laut_text.clients_tooltip_text_ClientsAlsaBufferbytes))
        Main_Layout.addLayout(StandardDropdownTemplate(laut_text.label_ClientsAlsaVolumeMethod,['cubic','linear'],laut_events.SetClientsAlsaVolumeMethod,defClientsAlsaVolumeMethod,laut_text.clients_tooltip_text_ClientsAlsaVolumeMethod))
        Main_Layout.setAlignment(Qt.AlignmentFlag.AlignTop)

        CurrentTab = QWidget()
        CurrentTab.setLayout(Main_Layout)
        ScrollArea = QScrollArea()
        ScrollArea.setWidget(CurrentTab)
        ScrollArea.setSizePolicy(QSizePolicy.Policy.Maximum,QSizePolicy.Policy.Expanding)
        ScrollArea.setWidgetResizable(True)

        return ScrollArea




        #alsa.deny = false
        #alsa.access = [ MMAP_INTERLEAVED MMAP_NONINTERLEAVED RW_INTERLEAVED RW_NONINTERLEAVED ]
        #alsa.format = [ FLOAT S32 S24 S24_3 S16 U8 ]
        #alsa.rate = { min=1 max=384000 }		# or [ 44100 48000 .. ]
        #alsa.channels = { min=1 max=64 }		# or [ 2 4 6 .. ]
        #alsa.period-bytes = { min=128 max=2097152 } # or [ 128 256 1024 .. ]
        #alsa.buffer-bytes = { min=256 max=4194304 } # or [ 256 512 4096 .. ]

        #alsa.volume-method = cubic			# linear, cubic


    def devices_panel(self):
        main_layout = QHBoxLayout()
        AllDevices = GetDevicesBasicInfo()
        for Device in AllDevices:
            device_sub_layout =  QVBoxLayout()

            device_text = QPlainTextEdit()
            device_text.setReadOnly(True)
            device_text.setProperty("class","device_text")
            device_sub_text = QPlainTextEdit()
            device_sub_text.setReadOnly(True)
            device_sub_text.setProperty("class","device_sub_text")

            device_name_label = QLabel()
            main_label = QLabel()
            properties_label = QLabel()
            main_label.setText("Device:")
            properties_label.setText("Properties:")
            device_name_label.setText(Device["device.description"].replace("\"",""))

            device_sub_layout.addWidget(main_label)
            device_sub_layout.addWidget(device_name_label)

            for key,DeviceParam in Device.items():
                device_text.appendPlainText(key + ": " + DeviceParam)

            Properties = GetDeviceCurrentProperties(Device)
            for Desc in Properties:
                for PropertyName,PropertyValue in Desc.items():
                    device_sub_text.appendPlainText(PropertyName + ": " + PropertyValue)

            device_sub_layout.addWidget(device_text)
            device_sub_layout.addWidget(properties_label)
            device_sub_layout.addWidget(device_sub_text)
            main_layout.addLayout(device_sub_layout)
        return main_layout

    ### subpanels
    def menu_buttons(self):
        save_button = StandardButtonTemplate("Save All\nConfiguration",QSize(100, 50),self.SaveConfiguration,laut_text.save_button_tooltip)
        reload_button = StandardButtonTemplate("Reload\nConfiguration",QSize(100, 50),self.ReloadConfiguration,laut_text.reload_button_tooltip)
        apply_button = StandardButtonTemplate("Apply\nConfiguration",QSize(100, 50),self.ApplyConfiguration,laut_text.apply_button_tooltip)

        whole = QHBoxLayout()
        whole.addWidget(save_button,alignment=Qt.AlignmentFlag.AlignLeft)
        whole.addWidget(reload_button,alignment=Qt.AlignmentFlag.AlignLeft)
        whole.addWidget(apply_button,alignment=Qt.AlignmentFlag.AlignLeft)

        return whole

    def submenu_version_display(self):

        main_layout = QVBoxLayout()
        versions_layout = QHBoxLayout()

        versions_layout.addWidget(AbsLableTemplate((laut_text.version_current + " " + str(GetPWVersion())),QSize(100, 24)))
        versions_layout.addWidget(AbsLableTemplate((laut_text.version_newest + " " + str(GetMostUpToDateVersion())),QSize(100, 24)))
        main_layout.addLayout(versions_layout)
        main_layout.addWidget(AbsLableTemplate((laut_text.version_disclamer),QSize(100, 24)))

        return main_layout

    ### Method & Functions ##
    #Cross File Methods

    def LoadConfigurationFromFile(self,configuration):
        if configuration == 'pipewire.conf':
            sub_configuration = 'pipewire_basic_properties.conf'
            if subConfigExitsCheck(sub_configuration,'pipewire.conf.d/'):
                prefix = GetConfigurationPath()
                prefix = prefix + 'pipewire.conf.d/'
                data = LoadPwJson(prefix,sub_configuration)
                if configuration == 'pipewire.conf':
                    properites_list = data[data.index('context.properties')+1]

                    RemoveOverrideProperties(properites_list)

                    return ParsePropertiesIntoDict(properites_list)

            elif ConfigExitsCheck(configuration) is True:
                prefix = GetConfigurationPath()
                data = LoadPwJson(prefix,configuration)
                if configuration == 'pipewire.conf':
                    properites_list = data[data.index('context.properties')+1]

                    RemoveOverrideProperties(properites_list)

                    return ParsePropertiesIntoDict(properites_list)

        if configuration == 'pipewire-pulse.conf':
            sub_configuration = 'pipewire-pulse_basic_properties.conf'
            if subConfigExitsCheck(sub_configuration,'pipewire-pulse.conf.d/'):
                prefix = GetConfigurationPath()
                prefix = prefix + 'pipewire-pulse.conf.d/'
                data = LoadPwJson(prefix,sub_configuration)
                stream_properties = data[data.index('stream.properties')+1]
                pulse_properties = data[data.index('pulse.properties')+1]

                RemoveOverrideProperties(pulse_properties)

                properites_list = pulse_properties + stream_properties

                return ParsePropertiesIntoDict(properites_list)
            elif ConfigExitsCheck(configuration) is True:
                prefix = GetConfigurationPath()
                data = LoadPwJson(prefix,configuration)
                stream_properties = data[data.index('stream.properties')+1]
                pulse_properties = data[data.index('pulse.properties')+1]

                RemoveOverrideProperties(pulse_properties)

                properites_list = pulse_properties + stream_properties

                return ParsePropertiesIntoDict(properites_list)

        if configuration == 'jack.conf':
            sub_configuration = 'jack_basic_properties.conf'
            if subConfigExitsCheck(sub_configuration,'pipewire-jack.conf.d/'):
                prefix = GetConfigurationPath()
                prefix = prefix + 'pipewire-jack.conf.d/'
                data = LoadPwJson(prefix,sub_configuration)
                jack_properties = data[data.index('jack.properties')+1]

                RemoveOverrideProperties(jack_properties)

                return ParsePropertiesIntoDict(jack_properties)

            elif ConfigExitsCheck(configuration) is True:
                prefix = GetConfigurationPath()
                data = LoadPwJson(prefix,configuration)
                jack_properties = data[data.index('jack.properties')+1]

                RemoveOverrideProperties(jack_properties)

                return ParsePropertiesIntoDict(jack_properties)

        if configuration == 'client-rt.conf':
            sub_configuration = 'client_basic_properties.conf'
            if subConfigExitsCheck(sub_configuration,'pipewire-client.conf.d/'):
                prefix = GetConfigurationPath()
                prefix = prefix + 'pipewire-client.conf.d/'
                data = LoadPwJson(prefix,sub_configuration)
                client_properties = data[data.index('stream.properties')+1]
                alsa_properties = data[data.index('alsa.properties')+1]

                alsa_rate_dict = { "alsa.rate": data[data.index('alsa.rate')+1]}
                alsa_channels_dict = { "alsa.channels": data[data.index('alsa.channels')+1]}
                alsa_period_dict = { "alsa.period-bytes": data[data.index('alsa.period-bytes')+1]}
                alsa_buffer_dict = { "alsa.buffer-bytes": data[data.index('alsa.buffer-bytes')+1]}
                #alsa.rate =
                #alsa.channels =
                #alsa.period-bytes
                #alsa.buffer-bytes
                combined_alsa_specific_props = alsa_rate_dict+alsa_channels_dict+alsa_period_dict+alsa_buffer_dict


                RemoveOverrideProperties(client_properties)

                properites_list = client_properties + alsa_properties + combined_alsa_specific_props

                return ParsePropertiesIntoDict(properites_list)

            elif ConfigExitsCheck(configuration) is True:
                prefix = GetConfigurationPath()
                data = LoadPwJson(prefix,configuration)
                client_properties = data[data.index('stream.properties')+1]
                alsa_properties = data[data.index('alsa.properties')+1]

                RemoveOverrideProperties(client_properties)
                properites_list = client_properties + alsa_properties

                return ParsePropertiesIntoDict(properites_list)


    def SaveConfigurationForPipewire(self):
        working_prefix = GetConfigurationPath() + 'pipewire.conf.d'
        SampleRate = laut_events.SampleRate if hasattr(laut_events,"SampleRate") else "48000"
        SampleAllowedRates = laut_events.SampleAllowedRates if hasattr(laut_events,"SampleAllowedRates") else "[ 44100 48000 88200 96000 176400 192000 352800 384000 ]"
        QuantumRate = laut_events.QuantumRate if hasattr(laut_events,"QuantumRate") else "2048"
        QuantumRate_min = laut_events.QuantumRate_min if hasattr(laut_events,"QuantumRate_min") else "512"
        QuantumRate_max = laut_events.QuantumRate_max if hasattr(laut_events,"QuantumRate_max") else "4096"
        QuantumRate_limit = laut_events.QuantumRate_limit if hasattr(laut_events,"QuantumRate_limit") else "8192"
        LinkBuffers_Max = laut_events.LinkBuffers_Max if hasattr(laut_events,"LinkBuffers_Max") else "16"

        parameters_list = {
            'clock-rate': SampleRate
            ,'allowed-rates': SampleAllowedRates
            ,'quantum-def': QuantumRate
            ,'quantum-min': QuantumRate_min
            ,'quantum-max': QuantumRate_max
            ,'quantum-limit': QuantumRate_limit
            ,'max-buffers': LinkBuffers_Max
        }


        to_be_saved = CreateConfigFilePipeWire(parameters_list)

        if not os.path.exists(working_prefix):
            os.makedirs(working_prefix)

        with open(working_prefix + '/pipewire_basic_properties.conf', 'w') as file:
            file.write(to_be_saved)

    def SaveConfigurationForPipewirePulse(self):
        working_prefix = GetConfigurationPath() + 'pipewire-pulse.conf.d/'
        PulseSample = laut_events.PulseSample if hasattr(laut_events,"PulseSample") else "48000"
        PulseFragMin = laut_events.PulseFragMin if hasattr(laut_events,"PulseFragMin") else "128"
        PulseFragDef = laut_events.PulseFragDef if hasattr(laut_events,"PulseFragDef") else "960"
        PulseReqMin = laut_events.PulseReqMin if hasattr(laut_events,"PulseReqMin") else "128"
        PulseReqDef = laut_events.PulseReqDef if hasattr(laut_events,"PulseReqDef") else "96000"
        PulseQuantMin = laut_events.PulseQuantMin if hasattr(laut_events,"PulseQuantMin") else "96000"
        PulseTLen = laut_events.PulseTLen if hasattr(laut_events,"PulseTLen") else "128"
        PulseNodesLatency = laut_events.PulseNodesLatency if hasattr(laut_events,"PulseNodesLatency") else "1024"
        PulseResamplingQuality = laut_events.PulseResamplingQuality if hasattr(laut_events,"PulseResamplingQuality") else "6"
        PulseDefaultFormat = laut_events.PulseDefaultFormat if hasattr(laut_events,"PulseDefaultFormat") else "F32"
        PulseDefaultPositon = laut_events.PulseDefaultPositon if hasattr(laut_events,"PulseDefaultPositon") else "[FR FL]"
        PulseIdleTimeout = laut_events.PulseIdleTimeout if hasattr(laut_events,"PulseIdleTimeout") else "0"


        parameters_list = {
             'arbitrary-sampling-param': PulseSample
            ,'pulse-min-req': PulseFragMin
            ,'pulse-default-req': PulseFragDef
            ,'pulse-min-frag': PulseReqMin
            ,'pulse-default-frag': PulseReqDef
            ,'pulse-default-tlength': PulseQuantMin
            ,'pulse-min-quantum': PulseTLen
            ,'node-latency-param': PulseNodesLatency
            ,'resample-quality-param': PulseResamplingQuality
            ,'pulse-idle-timeout': PulseDefaultFormat
            ,'pulse-default-format': PulseDefaultPositon
            ,'pulse-default-position': PulseIdleTimeout
        }

        to_be_saved = CreateConfigFilePipeWirePulse(parameters_list)

        if not os.path.exists(working_prefix):
            os.makedirs(working_prefix)

        with open(working_prefix + '/pulse_basic_properties.conf', 'w') as file:
            file.write(to_be_saved)

    def SaveConfigurationForPipewireJack(self):
        working_prefix = GetConfigurationPath() + 'pipewire-jack.conf.d/'
        JackSample = laut_events.JackSample if hasattr(laut_events,"JackSample") else "48000"
        JackNodeLatency = laut_events.JackNodeLatency if hasattr(laut_events,"JackNodeLatency") else "1024"
        JackNodeRate = laut_events.JackNodeRate if hasattr(laut_events,"JackNodeRate") else "1"

        JackNodeLockQuantum = laut_events.JackNodeLockQuantum if hasattr(laut_events,"JackNodeLockQuantum") else "True"
        JackNodeForceQuantum = laut_events.JackNodeForceQuantum if hasattr(laut_events,"JackNodeForceQuantum") else "0"
        JackshowMonitor = laut_events.JackshowMonitor if hasattr(laut_events,"JackshowMonitor") else "True"
        JackmergeMonitor = laut_events.JackmergeMonitor if hasattr(laut_events,"JackmergeMonitor") else "True"
        JackshowMidi = laut_events.JackshowMidi if hasattr(laut_events,"JackshowMidi") else "True"
        JackshortName = laut_events.JackshortName if hasattr(laut_events,"JackshortName") else "False"
        JackfilterName = laut_events.JackfilterName if hasattr(laut_events,"JackfilterName") else "False"
        JackfilterChar = laut_events.JackfilterChar if hasattr(laut_events,"JackfilterChar") else "\" \""
        JackselfConnect = laut_events.JackselfConnect if hasattr(laut_events,"JackselfConnect") else "allow"
        JacklockedProcess = laut_events.JacklockedProcess if hasattr(laut_events,"JacklockedProcess") else "True"
        JackdefaultAs = laut_events.JackdefaultAs if hasattr(laut_events,"JackdefaultAs") else "False"
        JackfixMidiEvents = laut_events.JackfixMidiEvents if hasattr(laut_events,"JackfixMidiEvents") else "True"
        JackglobalBufferSize = laut_events.JackglobalBufferSize if hasattr(laut_events,"JackglobalBufferSize") else "False"
        JackmaxClientPorts = laut_events.JackmaxClientPorts if hasattr(laut_events,"JackmaxClientPorts") else "768"
        JackfillAliases = laut_events.JackfillAliases if hasattr(laut_events,"JackfillAliases") else "False"
        JackwritableInput = laut_events.JackwritableInput if hasattr(laut_events,"JackwritableInput") else "True"

        parameters_list = {
                "arbitrary-sampling-param": JackSample
                ,"node.latency": JackNodeLatency
                ,"node.rate": JackNodeRate
                ,"node.lock-quantum": JackNodeLockQuantum
                ,"node.force-quantum": JackNodeForceQuantum
                ,"jack.show-monitor": JackshowMonitor
                ,"jack.merge-monitor": JackmergeMonitor
                ,"jack.show-midi": JackshowMidi
                ,"jack.short-name": JackshortName
                ,"jack.filter-name": JackfilterName
                ,"jack.filter-char": JackfilterChar
                ,"jack.self-connect-mode": JackselfConnect
                ,"jack.locked-process": JacklockedProcess
                ,"jack.default-as-system": JackdefaultAs
                ,"jack.fix-midi-events": JackfixMidiEvents
                ,"jack.global-buffer-size": JackglobalBufferSize
                ,"jack.max-client-ports": JackmaxClientPorts
                ,"jack.fill-aliases": JackfillAliases
                ,"jack.writable-input": JackwritableInput
        }

        to_be_saved = CreateConfigFilePipeWireJack(parameters_list)

        if not os.path.exists(working_prefix):
            os.makedirs(working_prefix)

        with open(working_prefix + '/jack_basic_properties.conf', 'w') as file:
            file.write(to_be_saved)

    def SaveConfigurationForPipewireClients(self):
        working_prefix = GetConfigurationPath() + 'pipewire-clients.conf.d/'
        
        SampleRateLoadedClients = laut_events.SampleRateLoadedClients if hasattr(laut_events,"SampleRateLoadedClients") else "48000"
        ClientsNodeLatency = laut_events.ClientsNodeLatency if hasattr(laut_events,"ClientsNodeLatency") else "1024"
        ClientsResampleQuality = laut_events.ClientsResampleQuality if hasattr(laut_events,"ClientsResampleQuality") else "6"
        ClientsChannelmixUpmixMethod = laut_events.ClientsChannelmixUpmixMethod if hasattr(laut_events,"ClientsChannelmixUpmixMethod") else "psd"
        ClientsChannelmixLfecutoff = laut_events.ClientsChannelmixLfecutoff if hasattr(laut_events,"ClientsChannelmixLfecutoff") else "150"
        ClientsChannelmixFccutoff = laut_events.ClientsChannelmixFccutoff if hasattr(laut_events,"ClientsChannelmixFccutoff") else "12000"
        ClientsChannelmixReardelay = laut_events.ClientsChannelmixReardelay if hasattr(laut_events,"ClientsChannelmixReardelay") else "12.0"
        ClientsChannelmixStereowiden = laut_events.ClientsChannelmixStereowiden if hasattr(laut_events,"ClientsChannelmixStereowiden") else "0.0"
        ClientsChannelmixHilberttaps = laut_events.ClientsChannelmixHilberttaps if hasattr(laut_events,"ClientsChannelmixHilberttaps") else "0"
        ClientsDitherNoise = laut_events.ClientsDitherNoise if hasattr(laut_events,"ClientsDitherNoise") else "0"
        ClientsNodeAutoconnect = laut_events.ClientsNodeAutoconnect if hasattr(laut_events,"ClientsNodeAutoconnect") else "true"
        ClientsChannelmixNormalize = laut_events.ClientsChannelmixNormalize if hasattr(laut_events,"ClientsChannelmixNormalize") else "false"
        ClientsChannelmixMixlfe = laut_events.ClientsChannelmixMixlfe if hasattr(laut_events,"ClientsChannelmixMixlfe") else "true"
        ClientsChannelmixUpmix = laut_events.ClientsChannelmixUpmix if hasattr(laut_events,"ClientsChannelmixUpmix") else "true"
        ClientsAlsaDeny = laut_events.ClientsAlsaDeny if hasattr(laut_events,"ClientsAlsaDeny") else "false"
        #ClientsAlsaAccess = laut_events.ClientsAlsaAccess if hasattr(laut_events,"ClientsAlsaAccess") else ""
        ClientsAlsaFormat = laut_events.ClientsAlsaFormat if hasattr(laut_events,"ClientsAlsaFormat") else "[ FLOAT S32 S24 S24_3 S16 U8 ]"
        ClientsAlsaRate = laut_events.ClientsAlsaRate if hasattr(laut_events,"ClientsAlsaRate") else "{ min=1 max=384000 }"
        ClientsAlsaChannels = laut_events.ClientsAlsaChannels if hasattr(laut_events,"ClientsAlsaChannels") else "{ min=1 max=64 }"
        ClientsAlsaPeriodbytes = laut_events.ClientsAlsaPeriodbytes if hasattr(laut_events,"ClientsAlsaPeriodbytes") else "{ min=128 max=2097152 }"
        ClientsAlsaBufferbytes = laut_events.ClientsAlsaBufferbytes if hasattr(laut_events,"ClientsAlsaBufferbytes") else "{ min=256 max=4194304 }"
        ClientsAlsaVolumeMethod = laut_events.ClientsAlsaVolumeMethod if hasattr(laut_events,"ClientsAlsaVolumeMethod") else "cubic"

        parameters_list = {
            "arbitrary-sampling-param": SampleRateLoadedClients
            ,"node.latency": ClientsNodeLatency
            ,"node.autoconnect": ClientsResampleQuality
            ,"resample.quality": ClientsChannelmixUpmixMethod
            ,"channelmix.normalize": ClientsChannelmixLfecutoff
            ,"channelmix.mix-lfe": ClientsChannelmixFccutoff
            ,"channelmix.upmix": ClientsChannelmixReardelay
            ,"channelmix.upmix-method": ClientsChannelmixStereowiden
            ,"channelmix.lfe-cutoff": ClientsChannelmixHilberttaps
            ,"channelmix.fc-cutoff": ClientsDitherNoise
            ,"channelmix.rear-delay": ClientsNodeAutoconnect
            ,"channelmix.stereo-widen": ClientsChannelmixNormalize
            ,"channelmix.hilbert-taps": ClientsChannelmixMixlfe
            ,"dither.noise": ClientsChannelmixUpmix
            ,"alsa.deny": ClientsAlsaDeny
            #,"alsa.access": ClientsAlsaAccess
            ,"alsa.format": ClientsAlsaFormat
            ,"alsa.rate": ClientsAlsaRate
            ,"alsa.channels": ClientsAlsaChannels
            ,"alsa.period-bytes": ClientsAlsaPeriodbytes
            ,"alsa.buffer-bytes": ClientsAlsaBufferbytes
            ,"alsa.volume-method": ClientsAlsaVolumeMethod
        }

        to_be_saved = CreateConfigFilePipeWireClients(parameters_list)

        if not os.path.exists(working_prefix):
            os.makedirs(working_prefix)

        with open(working_prefix + '/clients_basic_properties.conf', 'w') as file:
            file.write(to_be_saved)

    ### Actions
    def SaveCurrentConfig(self):
        self.SaveConfigurationForPipewire()
        self.SaveConfigurationForPipewirePulse()
        self.SaveConfigurationForPipewireJack()
        self.SaveConfigurationForPipewireClients()

    def RefreshCurrentDevices():
        pass
    def ApplyConfiguration(self):
        RestartPWServices()
        self.SaveCurrentConfig()
    def ReloadConfiguration(self):
        self.Pipewire_Configuration_Tab().update()
    def SaveConfiguration(self):
        self.SaveCurrentConfig()



    ### Initialize ###

path_to_stylesheet = os.path.dirname(os.path.realpath(__file__))

app = QApplication(sys.argv)

with open(path_to_stylesheet+"/styles.css","r") as file:
    app.setStyleSheet(file.read())

w = MainWindow()
w.show()

app.exec()

