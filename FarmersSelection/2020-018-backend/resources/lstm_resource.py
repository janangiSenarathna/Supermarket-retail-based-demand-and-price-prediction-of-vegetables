from flask_restful import Resource
# from predictions.lstm_model import LstmModel
from selection.farmers import optimizationModel
from flask import request

# class Predict(Resource):
#     def post(self):
#         data = request.get_json()
#         # print(data["date"])
#         prediction = LstmModel().get_prediction(data["test1"], data["test2"])
#         return prediction

class Select(Resource):
    def post(self):
        data = request.get_json()
        selections = optimizationModel().get_selections(data["test1"])
        # ,data["test2"],data["test3"])
        # ,data["test4"],data["test5"])
        return selections