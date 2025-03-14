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