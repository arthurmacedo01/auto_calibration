import time
import numpy as np  
import csv

class FrequencyAcquirer:

    def __init__(self,signalGenerator,params) -> None:
        self.signalGenerator = signalGenerator
        self.call(params)

    def call(self,params):

        ini_freq=params['ini_freq']
        freq_step=params['freq_step']
        final_freq=params['final_freq']
        ini_ampl=params['ini_ampl']
        ampl_step=params['ampl_step']
        final_ampl=params['final_ampl']
        n_readings=params['n_readings']
        interval=params['interval']

        if(freq_step == 0):
            final_freq=ini_freq
            freq_step=1
        if(ampl_step == 0):
            final_ampl=ini_ampl
            ampl_step=1
            
        self.signalGenerator.switchRF(True) # Turns the RF output on

        reading_array = []

        for freq in np.arange(ini_freq,final_freq+freq_step,freq_step):
            for ampl in np.arange(ini_ampl,final_ampl+ampl_step,ampl_step):
                for n in range(0,n_readings,1):                
                    self.signalGenerator.setAmplitude(ampl) # Sets the amplitude of the RF output to the desired <value> in dBm
                    self.signalGenerator.setFrequency(freq) # Sets the RF frequency to the <value> in MHz
                    read_amplitude = self.signalGenerator.getAmplitude() # Query the amplitude of the RF output
                    read_frequency = self.signalGenerator.getFrequency() # Query the RF frequency
                    time.sleep(interval) # sleep for <value> seconds                
                    reading_array.append([float(read_frequency.strip()),float(read_amplitude.strip())])    
        self.signalGenerator.switchRF(False) # Turns the RF output off
        fields = ['Frequência Gerada','Amplitude Gerada']
        
        self.__write_csv(fields, reading_array)
        

    def __write_csv(self, fields, rows):
        try:
            timestr = time.strftime("%Y%m%d_%H%M%S")
            filename = './outputs/output_{timestr}.csv'.format(timestr=timestr)
            with open(filename, 'w', newline='\n') as f:    
                # using csv.writer method from CSV package
                write = csv.writer(f,delimiter=';') 
                write.writerow(fields)
                write.writerows(rows)
        except:
            raise Exception("Não foi possível salvar o aquivo de saída. Verifique se o arquivo não está aberto.") 