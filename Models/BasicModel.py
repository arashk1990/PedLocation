# A basic model to predict next location of a pedestrian
import numpy as np
import pandas as pd
import math
class BaseModel:
    def __init__(self):
        self.t = 0.1  # time intervals to be observed
        self.speed = 1.2  # pedestrian default speed m/s
    def predict(self,org,dest):
        x1, y1 = org
        x2, y2 = dest
        angle = math.atan2(y2 - y1, x2 - x1)
        if angle == math.pi / 2:
            speedX = 0
        else:
            speedX = self.speed * math.cos(angle)
        speedY = self.speed * math.sin(angle)
        newX = speedX * self.t + x1
        newY = speedY * self.t + y1
        return (newX, newY)
