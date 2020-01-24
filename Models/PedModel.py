# A basic model to predict next location of a pedestrian
import numpy as np
import pandas as pd
import math
import pickle
import BasicModel


BasicModel.main()
with open('Model_V0.pkl', 'rb') as f:
    model_V0 = pickle.load(f)

position = {
    'x' : 0,
    'y' : 10
}
context = {
    'destination' : (10,10),
    'time interval' : 0.1,
    'speed m/s' : 1.2
}

def ped_model(context,position):
    org = (position['x'], position['y'])
    dest = context['destination']
    t = context['time interval']
    s = context['speed m/s']
    model = model_V0(t,s)
    new_x, new_y = model.predict(org,dest)
    output = {
        'x': new_x,
        'y': new_y}
    return output
