import pyvisa

class FrequencyInstrument:
  def __init__(self, address):
    rm = pyvisa.ResourceManager()
    self.visa_resource = rm.open_resource(address) #  gives you an instance of a subclass of the more generic Resource
    self.visa_resource.timeout = 1000 #  timeout is set in miliseconds.
    self.visa_resource.write('*RST') # Resets the signal generator to a default state
    self.idn = self.visa_resource.query('*IDN?') # Returns the instruments identity. 

  def getIdn(self):
    return self.idn # Returns the instruments identity. 

  def switchRF(self,switch):
    if(switch==True):
      self.visa_resource.write('OUTP:STAT ON') # Turns the RF output on
    else:
      self.visa_resource.write('OUTP:STAT OFF') # Turns the RF output off

  def setFrequency(self,freq):
    self.visa_resource.write('FREQ:CW {freq:.2f} MHZ'.format(freq=freq)) # Sets the RF frequency to the <value> and <units>

  def getFrequency(self):
    return self.visa_resource.query('FREQ:CW?') # Query the RF frequency

  def setAmplitude(self,ampl):
    return self.visa_resource.write('POW:AMPL {ampl:.2f} DBM'.format(ampl=ampl)) # Sets the amplitude of the RF output to the desired <value> and <units>

  def getAmplitude(self):            
    return self.visa_resource.query('POW:AMPL?') # Query the amplitude of the RF output