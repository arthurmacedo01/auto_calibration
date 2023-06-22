#  pip install pyvisa Flask waitress numpy python-dotenv
#  flask run --host=192.168.36.62  --port=3000

from flask import Flask, request
from dotenv import load_dotenv
import os
from controllers.HomeController import HomeController
from controllers.FreqAquisitionController import FreqAquisitionController

load_dotenv()
HOST_IP = os.environ.get("HOST_IP")
HOST_PORT = os.environ.get("HOST_PORT")
APP_SECRET_KEY = os.environ.get("APP_SECRET_KEY")
print(APP_SECRET_KEY)
app = Flask(__name__)
app.config['SECRET_KEY'] = APP_SECRET_KEY

@app.route("/")
def home_index():
    return HomeController.index()

@app.route("/freq_acquisitions", methods=('GET', 'POST'))
def freq_acquisition():        
    if(request.method=="POST"):
        return FreqAquisitionController.run()
    return FreqAquisitionController.index()

if __name__ == "__main__":
    from waitress import serve    
    serve(app, host=HOST_IP, port=HOST_PORT)