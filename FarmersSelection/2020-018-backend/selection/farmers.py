from werkzeug.security import generate_password_hash, check_password_hash
from flask import request
# from flask import json
import pandas as pd
import numpy as np
# from sklearn import model_selection
# from sklearn.linear_model import LogisticRegression
# from sklearn.decomposition import PCA
# from sklearn.preprocessing import scale
# import seaborn as sns
from ipywidgets import interact
from gurobipy import*
import pickle
import json

# from selection.preprocess_model import PreprocessModel

class optimizationModel():
    def get_selections(self, Demand):
    # , defective_rate, on_time):
    # Weighted_Score_Sum, Defective_rate, on_time_delivery_rate, supply_capacity, unit_price):

        
        loaded_model = pickle.load(open('Finalized_FarmerModel.sav', 'rb'))

        result = loaded_model.score(Demand)
        # defective_rate, on_time)
        # print ('loaded_model is', solutions)
        # , defective_rate, on_time)
            # Weighted_Score_Sum, Defective_rate, on_time_delivery_rate, supply_capacity, unit_price)
        return jsonify(result)


