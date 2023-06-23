from components.FrequencyInstrument import FrequencyInstrument
import pyvisa

class InstrumentSelector:
    def call(address):
        try:
            rm = pyvisa.ResourceManager()
            visa_resource = rm.open_resource(address)
            visa_resource.timeout = 1000 #  timeout is set in miliseconds.
            idn = visa_resource.query('*IDN?') # Returns the instruments identity. 
            model = idn.split(",")[1].strip()
            rm.close()
            match model:
                case "8648C":
                    return FrequencyInstrument(address)
                case _:
                    return FrequencyInstrument(address)
        except:
            raise Exception("Não foi possível se comunicar com o equipamento.")