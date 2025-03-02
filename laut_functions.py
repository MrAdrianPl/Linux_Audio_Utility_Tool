from pipewire_python.controller import Controller
import os
import requests

def GetDevicesBasicInfo():
    BasicDevicesInfo = []
    output = Controller().get_list_interfaces(type_interfaces = "Device")
    for dev in output:
        output.get(dev).get("properties")
        CurrentDeviceInfo = { key: data for key,data in output.get(dev).get("properties").items() if key in ('device.name','device.description','object.serial') }
        CurrentDeviceInfo.update({'device.id':dev})
        BasicDevicesInfo.append(CurrentDeviceInfo)
    return BasicDevicesInfo

def GetPWVersion():
    pipewire_version = os.popen('pipewire --version').readlines()
    x = pipewire_version[1].find("libpipewire")
    c_s = x+len("libpipewire")
    return pipewire_version[1][c_s:].strip()

def GetMostUpToDateVersion():
    response = requests.get("https://api.github.com/repos/PipeWire/pipewire/tags")
    return response.json()[0].get("name")

def GetDeviceCurrentProperties(DevName):
    PWTopOutput = os.popen(f'pw-top -b -n 3 | grep {DevName["device.description"].replace(" ","_")}|awk \'{{print $1,sep,$2,sep,$3,sep,$4,sep,$5,sep,$6,sep,$7,sep,$8,sep,$9,sep,$10,sep,$11,sep,$12,sep,$13; sep=";"}}\' ').read()
    #3 itterations are nessecary to retrive acctuall data from pw-top

    RemovableItters = PWTopOutput.splitlines()
    del RemovableItters[0:2]
    #remove garbage itters
    
    DevicesList = []

    OutputHeaders = ["S","ID","Quant","Rate","Wait","Busy","W/Q","B/Q","Error","Bit Format","Channels","Device Rate","Name"]
    #added custom headers

    if not PWTopOutput:
        OutputData = [["NaN","NaN","NaN","NaN","NaN","NaN","NaN","NaN","NaN","NaN","NaN","NaN","NaN"]]
    else:
        OutputData = [list(map(str.strip,x.split(";"))) for x in RemovableItters]
    #splits and removes extra spaces
        for device in OutputData:
            DevicesList.append({ key:value for (key,value) in zip(OutputHeaders,device) })
    return DevicesList

def GetConfigurationPath():
    home_path = os.path.expanduser('~')
    configurations_path = '/.config/pipewire/'
    return home_path + configurations_path

def ConfigExitsCheck(config_name:str):
    prefix = GetConfigurationPath()
    return os.path.isfile( prefix + config_name )

def subConfigExitsCheck(sub_config_name:str):
    prefix = GetConfigurationPath()
    config_extra = 'pipewire.conf.d/'
    return os.path.isfile( prefix + config_extra + sub_config_name )



def RestartPWServices():
    active_wireplumber = os.popen('systemctl --user status wireplumber').read()
    active_pipewire = os.popen('systemctl --user status pipewire').read()
    active_pipewire_pulse = os.popen('systemctl --user status pipewire-pulse').read()
    active_pipewire_jack = os.popen('systemctl --user status pipewire-jack').read()

    if active_wireplumber.startswith('● wireplumber.service'):
        print("Active Wireplumber")
        os.popen('systemctl --user restart wireplumber')
    if active_pipewire.startswith('● pipewire.service'):
        print("Active PW")
        os.popen('systemctl --user restart pipewire')
    if active_pipewire_pulse.startswith('● pipewire-pulse.service'):
        print("Active PW-Pulse")
        os.popen('systemctl --user restart pipewire-pulse')
    if active_pipewire_jack.startswith('● pipewire-jack.service'):
        print("Active PW-Jack")
        os.popen('systemctl --user restart pipewire-jack')


