from flask import Flask
from flask import Blueprint
from flask_restful import Api

# from resources.lstm_resource import Predict
from resources.lstm_resource import Select

# lstm_blueprint = Blueprint('lstm', __name__)
# lstm_blueprint_api = Api(lstm_blueprint)

# lstm_blueprint_api.add_resource(Predict, '/user', methods = ['POST'])
# lstm_blueprint_api.add_resource(Predict, '/lstm', methods = ['POST'])

farmer_blueprint = Blueprint('farmer', __name__)
farmer_blueprint_api = Api(farmer_blueprint)

farmer_blueprint_api.add_resource(Select, '/user', methods = ['POST'])
