# PedLocation:
A project to predict the next location of pedestrians.

**Phase 1**: A simple function called **BaseModel** gets Cartesian coordinates of origin and destination and proveds the next location of pedestrian after 0.1 second assuming a speed of 1.2 m/s for the pedestian. 
Usage:
```python
model = BaseModel()
newX, newY = model.predict((x1,y1),(x2,y2))
```

