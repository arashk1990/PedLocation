import pickle
import math

class Model_V0:
    def __init__(self,t, speed):
        self.t = t                              # time intervals to be observed
        self.speed = speed                          # pedestrian default speed (m/s)
    def predict(self,org,dest):
        x1, y1 = org                              #input: coordiantes of origin and destination
        x2, y2 = dest
        angle = math.atan2(y2 - y1, x2 - x1)      #angle of movement of pedestrian in radians

        if angle == math.pi / 2:                  #speed of ped projected to X and Y axis
            speedX = 0
        else:
            speedX = self.speed * math.cos(angle)
        speedY = self.speed * math.sin(angle)
        newX = speedX * self.t + x1
        newY = speedY * self.t + y1
        return (newX, newY)

def main():
    with open('Model_V0.pkl', 'wb') as f:
        pickle.dump(Model_V0,f)

if __name__=='__main__':
    main()
