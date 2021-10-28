From AdvancedModel.py import *

"""Returns a prediction based on the linear estimate model trained in AdvancedModel.py"""
def prediction(inputSet):
    pred = linear_est.predict(inputSet)
    return pred
