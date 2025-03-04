import sys
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
                            ,GetMostUpToDateVersion)
from laut_files_handling import LoadPwJson,CreateConfigFilePipeWire
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
        SampleRateLoaded = pipewire_data['default.clock.rate']
        AllowedRatesLoaded = pipewire_data['default.clock.allowed-rates']
        QuantumDefLoaded = pipewire_data['default.clock.quantum']
        QuantumMinLoaded = pipewire_data['default.clock.min-quantum']
        QuandumMaxLoaded = pipewire_data['default.clock.max-quantum']
        QuantumLimitLoaded = pipewire_data['default.clock.quantum-limit']
        LinkBuffersLoaded = pipewire_data['link.max-buffers']

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
        
        main_header_pulse = StandardLableTemplate(laut_text.main_header_pulse_txt,QSize(300, 40))
        main_header_pulse.setProperty("class","Settings_Header")
        Main_Layer = QVBoxLayout()
        Main_Layer.addWidget(main_header_pulse,alignment=Qt.AlignmentFlag.AlignTop)
        #Main_Layer.addLayout(StandardDropdownTemplate('Resampling Quality:',['1','2','3','4','5','6','7','8','9','10'],self.SetSampleRateValue,'6'))
        #pipewrie pulse latency
        #Pulse Quantum
        #Pulse samples
        main_header_pulse.setAlignment(Qt.AlignmentFlag.AlignCenter) 
        return Main_Layer   
 
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
            if subConfigExitsCheck(sub_configuration):
                prefix = GetConfigurationPath()
                prefix = prefix + 'pipewire.conf.d/'
                data = LoadPwJson(prefix,sub_configuration)
                if configuration == 'pipewire.conf':
                    properites_list = data[1]

                    if properites_list.count('vm.overrides = {')>0 :
                        rsi_s = properites_list.index('vm.overrides = {')
                        rsi_e = properites_list.index('}')

                        del properites_list[rsi_s:rsi_e+1]

                    return dict( list(map(str.strip,propert.split('='))) for propert in properites_list if len(propert.split('=')) > 1 )
            elif ConfigExitsCheck(configuration) is True:
                prefix = GetConfigurationPath()
                data = LoadPwJson(prefix,configuration)
                if configuration == 'pipewire.conf':
                    properites_list = data[1]

                    if properites_list.count('vm.overrides = {')>0 :
                        rsi_s = properites_list.index('vm.overrides = {')
                        rsi_e = properites_list.index('}')

                        del properites_list[rsi_s:rsi_e+1]

                    return dict( list(map(str.strip,propert.split('='))) for propert in properites_list if len(propert.split('=')) > 1 )
            else:
                parameters_list = {  
                    'default.clock.rate': "48000"
                    ,'default.clock.allowed-rates': "[ 44100 48000 88200 96000 176400 192000 352800 384000 ]"
                    ,'default.clock.quantum': "2048"
                    ,'default.clock.min-quantum': "512"
                    ,'default.clock.max-quantum': "4096"
                    ,'default.clock.quantum-limit': "8192" 
                    ,'max-buffers': "16"
                }
                return parameters_list

    def SaveConfigurationForPipewire(self):
        testing_prefix = '/media/mradrian/VMEnv/Python Programs/file_tests'
        working_prefix = GetConfigurationPath() + 'pipewire.conf.d/'
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
        with open(working_prefix + '/pipewire_basic_properties.conf', 'w') as file:
            file.write(to_be_saved)


    ### Actions
    def SaveCurrentConfig(self):
        self.SaveConfigurationForPipewire()
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

