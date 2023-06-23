from flask import render_template, request, flash
from services.FrequencyAcquirer import FrequencyAcquirer
from services.InstrumentSelector import InstrumentSelector
from services.IntrumentDiscover import IntrumentDiscover
import pyvisa

class FreqAquisitionController():

    def index():
        active_resource_list = IntrumentDiscover.call()         
        return render_template('settings_index.html',active_resource_list = active_resource_list)
    
    def run():
        params = FreqAquisitionController.__read_params(request.form)
        try:
            signal_generator_adress = FreqAquisitionController.__get_signal_generator_adress(request.form)
            signalGenerator = InstrumentSelector.call(signal_generator_adress)
            FrequencyAcquirer(signalGenerator, params)
            return render_template('settings_success.html')
        except pyvisa.errors.VisaIOError as error:
            flash('Falha ao executar rotina! Verifique a conexão e os parâmetros.\n{}'.format(error))
            return render_template('settings_index.html')
        except Exception as error:
            flash(error)
            return render_template('settings_index.html')

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
    def __get_signal_generator_adress(parms_input):    
        return parms_input['signal_generator']
