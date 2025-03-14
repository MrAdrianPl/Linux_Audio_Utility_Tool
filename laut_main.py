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
                             ,QGridLayout)
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
                            ,my_coalesce)
from laut_files_handling import LoadPwJson,CreateConfigFilePipeWire,CreateConfigFilePipeWirePulse
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
        minl = QGridLayout()
        topl = QHBoxLayout()
        midl = self.pipewire_pulse_panel()
        midls = self.pipewire_settings_panel_pw()
        midld = self.pipewire_jack_panel()
        midlt = self.pipewire_alsa_panel()
        bottml = QHBoxLayout()

        topl.addLayout(self.menu_buttons())
        bottml.addLayout(self.submenu_version_display())
        #verticalSpacer = QtWidgets.QSpacerItem(40, 20,  QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding) grid.addItem(verticalSpacer, 6, 0, QtCore.Qt.AlignTop)

        minl.addLayout(topl,0,0,)
        minl.addLayout(midls,1,0,Qt.AlignmentFlag.AlignTop)
        minl.addLayout(midl,1,1,Qt.AlignmentFlag.AlignTop)
        minl.addLayout(midld,1,2,Qt.AlignmentFlag.AlignTop)
        minl.addLayout(midlt,1,3,Qt.AlignmentFlag.AlignTop)
        minl.addLayout(bottml,2,0)

        Pipewire_Configuration_Tab_win = QWidget()
        Pipewire_Configuration_Tab_win.setLayout(minl)
        return Pipewire_Configuration_Tab_win     
    
    def Alsa_Configuration_Tab(self):

        minl = QHBoxLayout()

        Alsa_Configuration_Tab_win = QWidget()
        Alsa_Configuration_Tab_win.setLayout(minl)
        return Alsa_Configuration_Tab_win

    ### panels

    def pipewire_settings_panel_pw(self):

        pipewire_data = self.LoadConfigurationFromFile('pipewire.conf')
        
        ###get Config Values###
        SampleRateLoaded = pipewire_data['default.clock.rate'] if pipewire_data.get('default.clock.rate') is not None else "48000"
        AllowedRatesLoaded = pipewire_data['default.clock.allowed-rates'] if pipewire_data.get('default.clock.allowed-rates') is not None else "[ 44100 48000 88200 96000 176400 192000 352800 384000 ]"
        QuantumDefLoaded = pipewire_data['default.clock.quantum'] if pipewire_data.get('default.clock.quantum') is not None else "2048"
        QuantumMinLoaded = pipewire_data['default.clock.min-quantum'] if pipewire_data.get('default.clock.min-quantum') is not None else "512"
        QuandumMaxLoaded = pipewire_data['default.clock.max-quantum'] if pipewire_data.get('default.clock.max-quantum') is not None else "4096"
        QuantumLimitLoaded = pipewire_data['default.clock.quantum-limit'] if pipewire_data.get('default.clock.quantum-limit') is not None else "8192" 
        LinkBuffersLoaded = pipewire_data['link.max-buffers'] if pipewire_data.get('link.max-buffers') is not None else "16"


        main_header_pw = StandardLableTemplate(laut_text.main_header_pipewire_txt,QSize(300, 40))
        main_header_pw.setProperty("class","Settings_Header")

        Main_Layout = QVBoxLayout()
        main_header_pw.setToolTip(laut_text.pwmain_tooltip_text)
        Main_Layout.addWidget(main_header_pw,alignment=Qt.AlignmentFlag.AlignTop)
        
        Lable_space = QHBoxLayout()

        

        Lable_space.addWidget(StandardLableTemplate("Sampling Settings:",QSize(120, 50)))
        Lable_space.addWidget(info_icon(36,36,laut_text.sample_tooltip_text),alignment=Qt.AlignmentFlag.AlignAbsolute)
               
        Main_Layout.addLayout(Lable_space)

        
        Main_Layout.addLayout(StandardDropdownTemplate('Sample Rate:',['16000','32000','44100','48000','88200','96000','176400','192000','352800','384000'],laut_events.SetSampleRateValue,str(SampleRateLoaded),laut_text.sample_rate_tooltip_text))
        Main_Layout.addLayout(StandardInputTemplate('Allowed Sampling Rates:',QSize(400, 28),laut_events.SetSampleAllowedRatesValue,str(AllowedRatesLoaded),laut_text.allowed_sample_tooltip_text))

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
        return Main_Layout

    def pipewire_alsa_panel(self):
        main_header_alsa = StandardLableTemplate(laut_text.main_header_clients_txt,QSize(300, 40))
        main_header_alsa.setProperty("class","Settings_Header")
        Main_Layer = QVBoxLayout()     
        Main_Layer.addWidget(main_header_alsa,alignment=Qt.AlignmentFlag.AlignTop)
        #Main_Layer.addLayout(StandardCheckboxTemplate('Suspend Idle Nodes:',self.SetQuantumDefValue))
        #Enable/Disable Idle Kill checkbox
        main_header_alsa.setAlignment(Qt.AlignmentFlag.AlignCenter)        
        return Main_Layer     
 
    def pipewire_pulse_panel(self):
        #add warning icon with tooltip about above settings\
        
        pipewire_pulse_data = self.LoadConfigurationFromFile('pipewire-pulse.conf')
        
        ###get Config Values###


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
          
        try: 
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

        main_header_pulse = StandardLableTemplate(laut_text.main_header_pulse_txt,QSize(300, 40))
        main_header_pulse.setProperty("class","Settings_Header")
        Main_Layout = QVBoxLayout()
        Main_Layout.addWidget(main_header_pulse,alignment=Qt.AlignmentFlag.AlignTop)

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

        main_header_pulse.setAlignment(Qt.AlignmentFlag.AlignCenter) 
        return Main_Layout   
 
    def pipewire_jack_panel(self):
        main_header_jack = StandardLableTemplate(laut_text.main_header_pipewire_txt,QSize(300, 40))
        main_header_jack.setProperty("class","Settings_Header")   
        Main_Layer = QVBoxLayout()
        Main_Layer.addWidget(main_header_jack,alignment=Qt.AlignmentFlag.AlignTop)
        main_header_jack.setAlignment(Qt.AlignmentFlag.AlignCenter)
        return Main_Layer

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
        save_button = StandardButtonTemplate("Save \nConfiguration",QSize(100, 50),self.SaveConfiguration,laut_text.save_button_tooltip)
        reload_button = StandardButtonTemplate("Reload \nConfiguration",QSize(100, 50),self.ReloadConfiguration,laut_text.reload_button_tooltip)
        apply_button = StandardButtonTemplate("Apply \nConfiguration",QSize(100, 50),self.ApplyConfiguration,laut_text.apply_button_tooltip)

        whole = QHBoxLayout()
        whole.addWidget(save_button,alignment=Qt.AlignmentFlag.AlignLeft)
        whole.addWidget(reload_button,alignment=Qt.AlignmentFlag.AlignLeft)
        whole.addWidget(apply_button,alignment=Qt.AlignmentFlag.AlignLeft)
        
        return whole
    
    def submenu_version_display(self):
        
        main_layout = QVBoxLayout()
        versions_layout = QHBoxLayout()

        versions_layout.addWidget(AbsLableTemplate((laut_text.version_current + " " + str(GetPWVersion())),QSize(300, 24)))
        versions_layout.addWidget(AbsLableTemplate((laut_text.version_newest + " " + str(GetMostUpToDateVersion())),QSize(300, 24)))
        main_layout.addLayout(versions_layout)
        main_layout.addWidget(AbsLableTemplate((laut_text.version_disclamer),QSize(300, 24)))
        
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

                    if properites_list.count('vm.overrides = {')>0 :
                        rsi_s = properites_list.index('vm.overrides = {')
                        rsi_e = properites_list.index('}')

                        del properites_list[rsi_s:rsi_e+1]

                    return dict( list(map(str.strip,propert.split('='))) for propert in properites_list if len(propert.split('=')) > 1 )
            elif ConfigExitsCheck(configuration) is True:
                prefix = GetConfigurationPath()
                data = LoadPwJson(prefix,configuration)
                if configuration == 'pipewire.conf':
                    properites_list = data[data.index('context.properties')+1]

                    if properites_list.count('vm.overrides = {')>0 :
                        rsi_s = properites_list.index('vm.overrides = {')
                        rsi_e = properites_list.index('}')

                        del properites_list[rsi_s:rsi_e+1]

                    return dict( list(map(str.strip,propert.split('='))) for propert in properites_list if len(propert.split('=')) > 1 )

        if configuration == 'pipewire-pulse.conf':
            sub_configuration = 'pipewire-pulse_basic_properties.conf'
            if subConfigExitsCheck(sub_configuration,'pipewire-pulse.conf.d/'):
                prefix = GetConfigurationPath()
                prefix = prefix + 'pipewire-pulse.conf.d/'
                data = LoadPwJson(prefix,sub_configuration)
                stream_properties = data[data.index('stream.properties')+1]
                pulse_properties = data[data.index('pulse.properties')+1]

                if pulse_properties.count('vm.overrides = {')>0 :
                    rsi_s = pulse_properties.index('vm.overrides = {')
                    rsi_e = pulse_properties.index('}')

                    del pulse_properties[rsi_s:rsi_e+1]       
                
                properites_list = pulse_properties + stream_properties

                return dict( list(map(str.strip,propert.split('='))) for propert in properites_list if len(propert.split('=')) > 1 ) 
            elif ConfigExitsCheck(configuration) is True:    
                prefix = GetConfigurationPath()
                data = LoadPwJson(prefix,configuration)
                stream_properties = data[data.index('stream.properties')+1]
                pulse_properties = data[data.index('pulse.properties')+1]

                if pulse_properties.count('vm.overrides = {')>0 :
                    rsi_s = pulse_properties.index('vm.overrides = {')
                    rsi_e = pulse_properties.index('}')

                    del pulse_properties[rsi_s:rsi_e+1]       
                
                properites_list = pulse_properties + stream_properties

                return dict( list(map(str.strip,propert.split('='))) for propert in properites_list if len(propert.split('=')) > 1 )                 


    def SaveConfigurationForPipewire(self):
        testing_prefix = '/media/mradrian/VMEnv/Python Programs/file_tests'
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
        testing_prefix = '/media/mradrian/VMEnv/Python Programs/file_tests'
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





    ### Actions
    def SaveCurrentConfig(self):
        self.SaveConfigurationForPipewire()
        self.SaveConfigurationForPipewirePulse()
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


app = QApplication(sys.argv)

with open("styles.css","r") as file:
    app.setStyleSheet(file.read())

w = MainWindow()
w.show()

app.exec()

