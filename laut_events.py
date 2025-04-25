### Eevents ###
def SetSampleRateValue(ratevalue) -> int:
    global SampleRate
    SampleRate = ratevalue
    print('SampleRate set to: ' + ratevalue)
def SetSampleAllowedRatesValue(ratevalue):
    global SampleAllowedRates
    SampleAllowedRates = ratevalue
    print('Sample Allowed Rates set to: ' + str(ratevalue))
def SetQuantumDefValue(value) -> int:
    global QuantumRate
    QuantumRate = value
    print('Quantum Def to: ' + value)
def SetQuantumMinValue(value) -> int:
    global QuantumRate_min
    QuantumRate_min = value
    print('Quantum Min to: ' + value)
def SetQuantumMaxValue(value) -> int:
    global QuantumRate_max
    QuantumRate_max = value
    print('Quantum Max to: ' + value)
def SetQuantumLimitValue(value) -> int:
    global QuantumRate_limit
    QuantumRate_limit = value
    print('Quantum Limit to: ' + value)
def SetBuffersMaxLinkBuffers(value) -> int:
    global LinkBuffers_Max
    LinkBuffers_Max = value
    print('Link Buffers Max to: ' + value)

def SetVoidPlaceholder(value) -> int:
    
    print('Placeholder: ' + value)

def SetPulseSample(value) -> int:
    global PulseSample
    PulseSample = value
    print('Pulse Sample: ' + value)
def SetPulseFragMin(value) -> int:
    global PulseFragMin
    PulseFragMin = value
    print('Pulse FragMin: ' + value)
def SetPulseFragDef(value) -> int:
    global PulseFragDef
    PulseFragDef = value
    print('Pulse FragDef: ' + value)
def SetPulseReqMin(value) -> int:
    global PulseReqMin
    PulseReqMin = value
    print('Pulse ReqMin: ' + value)
def SetPulseReqDef(value) -> int:
    global PulseReqDef
    PulseReqDef = value
    print('Pulse ReqDef: ' + value)
def SetPulseQuantMin(value) -> int:
    global PulseQuantMin
    PulseQuantMin = value
    print('Pulse QuantMin: ' + value)
def SetPulseTLen(value) -> int:
    global PulseTLen
    PulseTLen = value
    print('Pulse TLen:' + value)                        
def SetPulseNodesLatency(value) -> int:
    global PulseNodesLatency
    PulseNodesLatency = value
    print('Pulse TLen:' + value)
def SetPulseResamplingQuality(value) -> int:
    global PulseResamplingQuality
    PulseResamplingQuality = value
    print('Pulse TLen:' + value)
def SetPulseDefaultFormat(value) -> int:
    global PulseDefaultFormat
    PulseDefaultFormat = value
    print('Pulse TLen:' + value)
def SetPulseDefaultPositon(value) -> int:
    global PulseDefaultPositon
    PulseDefaultPositon = value
    print('Pulse TLen:' + value)
def SetPulseIdleTimeout(value) -> int:
    global PulseIdleTimeout
    PulseIdleTimeout = value
    print('Pulse TLen:' + value)    

def SetJackSample(value) -> int:
    global JackSample
    JackSample = value
    print('JackSample:' + str(value))

def SetJackNodeLatency(value) -> int:
    global JackNodeLatency
    JackNodeLatency = value
    print('JackNodeLatency:' + str(value))

def SetJackNodeRate(value) -> int:
    global JackNodeRate
    JackNodeRate = value
    print('JackNodeRate:' + str(value))

def SetJackNodeQuantum(value) -> int:
    global JackNodeQuantum
    JackNodeQuantum = value
    print('JackNodeQuantum:' + str(value))

def SetJackNodeLockQuantum(value) -> int:
    global JackNodeLockQuantum
    if str(value) == 'CheckState.Checked':
        JackNodeLockQuantum = "true"
    else: 
        JackNodeLockQuantum = "false"
    print('JackNodeLockQuantum:' + JackNodeLockQuantum)

def SetJackNodeForceQuantum(value) -> int:
    global JackNodeForceQuantum
    if str(value) == 'CheckState.Checked':
        JackNodeForceQuantum = "true"
    else: 
        JackNodeForceQuantum = "false"
    print('JackNodeForceQuantum:' + JackNodeForceQuantum)

def SetJackshowMonitor(value) -> int:
    global JackshowMonitor
    if str(value) == 'CheckState.Checked':
        JackshowMonitor = "true"
    else: 
        JackshowMonitor = "false"
    print('JackshowMonitor:' + JackshowMonitor)

def SetJackmergeMonitor(value) -> int:
    global JackmergeMonitor
    if str(value) == 'CheckState.Checked':
        JackmergeMonitor = "true"
    else: 
        JackmergeMonitor = "false"
    print('JackmergeMonitor:' + JackmergeMonitor)

def SetJackshowMidi(value) -> int:
    global JackshowMidi
    if str(value) == 'CheckState.Checked':
        JackshowMidi = "true"
    else: 
        JackshowMidi = "false"
    print('JackshowMidi:' + JackshowMidi)

def SetJackshortName(value) -> int:
    global JackshortName
    if str(value) == 'CheckState.Checked':
        JackshortName = "true"
    else: 
        JackshortName = "false"
    print('JackshortName:' + JackshortName)

def SetJackfilterName(value) -> int:
    global JackfilterName
    if str(value) == 'CheckState.Checked':
        JackfilterName = "true"
    else: 
        JackfilterName = "false"
    print('JackfilterName:' + JackfilterName)

def SetJackfilterChar(value) -> int:
    global JackfilterChar
    JackfilterChar = value
    print('JackfilterChar:' + str(value))

def SetJackselfConnect(value) -> int:
    global JackselfConnect
    JackselfConnect = value
    print('JackselfConnect:' + str(value))

def SetJacklockedProcess(value) -> int:
    global JacklockedProcess
    if str(value) == 'CheckState.Checked':
        JacklockedProcess = "true"
    else: 
        JacklockedProcess = "false"
    print('JacklockedProcess:' + JacklockedProcess)

def SetJackdefaultAs(value) -> int:
    global JackdefaultAs
    if str(value) == 'CheckState.Checked':
        JackdefaultAs = "true"
    else: 
        JackdefaultAs = "false"
    print('JackdefaultAs:' + JackdefaultAs)

def SetJackfixMidiEvents(value) -> int:
    global JackfixMidiEvents
    if str(value) == 'CheckState.Checked':
        JackfixMidiEvents = "true"
    else: 
        JackfixMidiEvents = "false"
    print('JackfixMidiEvents:' + JackfixMidiEvents)

def SetJackglobalBufferSize(value) -> int:
    global JackglobalBufferSize
    if str(value) == 'CheckState.Checked':
        JackglobalBufferSize = "true"
    else: 
        JackglobalBufferSize = "false"
    print('JackglobalBufferSize:' + JackglobalBufferSize)

def SetJackmaxClientPorts(value) -> int:
    global JackmaxClientPorts
    JackmaxClientPorts = value
    print('JackmaxClientPorts:' + str(value))

def SetJackfillAliases(value) -> int:
    global JackfillAliases
    if str(value) == 'CheckState.Checked':
        JackfillAliases = "true"
    else: 
        JackfillAliases = "false"
    print('JackfillAliases:' + JackfillAliases)

def SetJackwritableInput(value) -> int:
    global JackwritableInput
    if str(value) == 'CheckState.Checked':
        JackwritableInput = "true"
    else: 
        JackwritableInput = "false"
    print('JackwritableInput:' + JackwritableInput) 

def SetSampleRateLoadedClients(value) -> int:
    global SampleRateLoadedClients
    SampleRateLoadedClients = value
    print('SetSampleRateLoadedClients:' + str(value))
def SetClientsNodeLatency(value) -> int:
    global ClientsNodeLatency
    ClientsNodeLatency = value
    print('SetClientsNodeLatency:' + str(value))
def SetClientsResampleQuality(value) -> int:
    global ClientsResampleQuality
    ClientsResampleQuality = value
    print('SetClientsResampleQuality:' + str(value))
def SetClientsChannelmixUpmixMethod(value) -> int:
    global ClientsChannelmixUpmixMethod
    ClientsChannelmixUpmixMethod = value
    print('SetClientsChannelmixUpmixMethod:' + str(value))
def SetClientsChannelmixLfecutoff(value) -> int:
    global ClientsChannelmixLfecutoff
    ClientsChannelmixLfecutoff = value
    print('SetClientsChannelmixLfecutoff:' + str(value))
def SetClientsChannelmixFccutoff(value) -> int:
    global ClientsChannelmixFccutoff
    ClientsChannelmixFccutoff = value
    print('SetClientsChannelmixFccutoff:' + str(value))
def SetClientsChannelmixReardelay(value) -> int:
    global ClientsChannelmixReardelay
    ClientsChannelmixReardelay = value
    print('SetClientsChannelmixReardelay:' + str(value))
def SetClientsChannelmixStereowiden(value) -> int:
    global ClientsChannelmixStereowiden
    ClientsChannelmixStereowiden = value
    print('SetClientsChannelmixStereowiden:' + str(value))
def SetClientsChannelmixHilberttaps(value) -> int:
    global ClientsChannelmixHilberttaps
    ClientsChannelmixHilberttaps = value
    print('SetClientsChannelmixHilberttaps:' + str(value))
def SetClientsDitherNoise(value) -> int:
    global ClientsDitherNoise
    ClientsDitherNoise = value
    print('SetClientsDitherNoise:' + str(value))

def SetClientsNodeAutoconnect(value) -> int:
    global ClientsNodeAutoconnect
    if str(value) == 'CheckState.Checked':
        ClientsNodeAutoconnect = "true"
    else: 
        ClientsNodeAutoconnect = "false"
    print('ClientsNodeAutoconnect:' + ClientsNodeAutoconnect) 
def SetClientsChannelmixNormalize(value) -> int:
    global ClientsChannelmixNormalize
    if str(value) == 'CheckState.Checked':
        ClientsChannelmixNormalize = "true"
    else: 
        ClientsChannelmixNormalize = "false"
    print('ClientsChannelmixNormalize:' + ClientsChannelmixNormalize) 
def SetClientsChannelmixMixlfe(value) -> int:
    global ClientsChannelmixMixlfe
    if str(value) == 'CheckState.Checked':
        ClientsChannelmixMixlfe = "true"
    else: 
        ClientsChannelmixMixlfe = "false"
    print('ClientsChannelmixMixlfe:' + ClientsChannelmixMixlfe) 
def SetClientsChannelmixUpmix(value) -> int:
    global ClientsChannelmixUpmix
    if str(value) == 'CheckState.Checked':
        ClientsChannelmixUpmix = "true"
    else: 
        ClientsChannelmixUpmix = "false"
    print('ClientsChannelmixUpmix:' + ClientsChannelmixUpmix)             

def SetClientsAlsaDeny(value) -> int:
    global ClientsAlsaDeny
    if str(value) == 'CheckState.Checked':
        ClientsAlsaDeny = "true"
    else: 
        ClientsAlsaDeny = "false"
    print('ClientsChannelmixUpmix:' + ClientsAlsaDeny)  

def SetClientsAlsaAccess(value) -> int:
    global ClientsAlsaAccess
    ClientsAlsaAccess = value
    print('ClientsAlsaAccess:' + value)
def SetClientsAlsaFormat(value) -> int:
    global ClientsAlsaFormat
    ClientsAlsaFormat = value
    print('ClientsAlsaFormat:' + value)
def SetClientsAlsaRate(value) -> int:
    global ClientsAlsaRate
    ClientsAlsaRate = value
    print('ClientsAlsaRate:' + value)
def SetClientsAlsaChannels(value) -> int:
    global ClientsAlsaChannels
    ClientsAlsaChannels = value
    print('ClientsAlsaChannels:' + value)
def SetClientsAlsaPeriodbytes(value) -> int:
    global ClientsAlsaPeriodbytes
    ClientsAlsaPeriodbytes = value
    print('ClientsAlsaPeriodbytes:' + value)
def SetClientsAlsaBufferbytes(value) -> int:
    global ClientsAlsaBufferbytes
    ClientsAlsaBufferbytes = value
    print('ClientsAlsaBufferbytes:' + value)
def SetClientsAlsaVolumeMethod(value) -> int:
    global ClientsAlsaVolumeMethod
    ClientsAlsaVolumeMethod = value
    print('ClientsAlsaVolumeMethod:' + value)