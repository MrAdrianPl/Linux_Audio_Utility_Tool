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