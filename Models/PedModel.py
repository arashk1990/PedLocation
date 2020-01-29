######################################
#  Date Created: January 28, 2020    #
#  Date Modified: Janaury 29, 2020   #
#  Ownership: LiTrans                #
#  Creator: Arash Kalatian           #
######################################
# A basic model to predict next location of a pedestrian
import numpy as np
import pandas as pd
import math
import pickle
import BasicModel

BasicModel.main()
with open('Model_V0.pkl', 'rb') as f:
    model_V0 = pickle.load(f)

# Load position and context from local text files and convert them to dictionaries,
# needs to be replaced by !Important desired format
context = {}
with open("/logs/Context") as f:
    for line in f:
        (key, val) = line.split(' : ')
        context[key] = val[:-1]
Xn, Yn = map(float, context['Destination'].replace(')', '').replace('(', '').split(','))
context['Destination'] = np.array((Xn, Yn))

Positions = {}
with open("/logs/Position") as f:
    for line in f:
        (key, val) = line.split(' : ')
        x, y = map(float, val.replace(')', '').replace('(', '').split(','))
        Positions[key] = (x, y)
org = Positions[list(Positions.keys())[0]]       # calling the first position in the list as origin
pos = Positions[list(Positions.keys())[-1]]      # calling the last position in the list as current location


def ped_model(context, position):
    dest = context['Destination']
    t = float(context['Time interval (s)'])
    s = float(context['Speed (m/s)'])
    model = model_V0(t, s)
    newPos = np.array(model.predict(position, dest))
    if np.linalg.norm(newPos - org) < np.linalg.norm(dest - org):     #check if the user has reached the destination
        output = newPos
    else:
        output = dest

    return output


output = ped_model(context, pos)

with open("/logs/Position", "a") as f:
    f.write("\nPosition {} : ({:.2f},{:.2f})".format(len(Positions), output[0], output[1]))
