# PedLocation:
A project to predict the next location of pedestrians.

**Phase 1**: A simple function called **ped_model** gets Cartesian coordinates of origin, as called _position_, and destination, speed and desired time intervals, as called _context_, and proveds the next location of pedestrian.
Default Values: speed: 1.2 m/s, intervals: 0.1 sec, 
Usage:
```python
output = ped_model(context, position)
```
in which:
```python
position = {'x': current X, 'y': current Y}
context = {'destination': final position, 'time interval': t, 'speed m/s' : s}
output = { 'x' : new X,
           'y: new Y}

