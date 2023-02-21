from flask import Flask
from pyctuator.pyctuator import Pyctuator

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'hello world'

py_actuator = Pyctuator(
    app,
    "Example pyactuator flask",
    app_url="http://localhost:8000",
    pyctuator_endpoint_url="http://localhost:8000/pyactuator",
    registration_url=None
)

@app.route('/healthz/liveness')
def liveness():
    return {'live': 'up'}

@app.route('/healthz/readiness')
def readiness():
    return {'ready': 'up'}
