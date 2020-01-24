# A basic model to predict next location of a pedestrian
import numpy as np
import pandas as pd
import math
import pickle

# Temporarily placing code here - for testing
with open ('BaseModel', 'rb') as f:
    BaseModel = pickle.load(f)
def ped_model(context,position):
    org = (position['x'], position['y'])
    dest = context['destination']
    model = BaseModel()
    new_x, new_y = model.predict(org,dest)
    output['x']
    return out


print("Simple Prediction: ")
print("origin:      (" + str(org[0])  + ", " + str(org[1])  + ")")
print("destination: (" + str(dest[0]) + ", " + str(dest[1]) + ")")
print("prediction:  (" + str(pred[0]) + ", " + str(pred[1]) + ")")
