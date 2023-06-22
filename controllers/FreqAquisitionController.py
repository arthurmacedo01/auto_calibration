from flask import render_template, request, flash
from services.FrequencyAcquirer import FrequencyAcquirer
from components.FrequencyInstrument import FrequencyInstrument
import pyvisa

class FreqAquisitionController():

    def index():        
        return render_template('settings_index.html')
    
    def run():
        params = FreqAquisitionController.__read_params(request.form)
        try:
            signalGenerator = FrequencyInstrument("GPIB0::19::INSTR")
            FrequencyAcquirer(signalGenerator, params)
            return render_template('settings_success.html')
        except pyvisa.errors.VisaIOError as error:
            flash('Falha ao executar rotina! Verifique a conexão e os parâmetros.\n{}'.format(error))
        except Exception as error:
            flash(error)
        


    # Auxiliar functions
    def __read_params(parms_input):
        params = {
            'ini_freq':float(parms_input['ini_freq']),
            'freq_step':float(parms_input['freq_step']),
            'final_freq':float(parms_input['final_freq']),
            'ini_ampl':float(parms_input['ini_ampl']),
            'ampl_step':float(parms_input['ampl_step']),
            'final_ampl':float(parms_input['final_ampl']),
            'n_readings':int(parms_input['n_readings']),
            'interval':float(parms_input['interval']),
        }
        return params