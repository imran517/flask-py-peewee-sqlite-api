from flask import Flask
from config import config

api = Flask(__name__)

from controller import *

if __name__ == '__main__':
    api.run(debug=True, port=config.api.port())