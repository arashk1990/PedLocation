# PedLocation:
A project to predict the next location of pedestrians.

**Phase 1**: A simple function called **ped_model** gets Cartesian coordinates of origin, as called _position_, and destination, speed and desired time intervals, as called _context_, and proveds the next location of pedestrian.
Context and Position text files are accessable in /logs folder
Usage in docker:
```python
To run PedModel.py in the docker, run the following commands in terminal/command prompt
in the directory of the docker file: ~/PedLocation/Models
sudo docker build -t python-barcode .    #(“.” is required.)
sudo docker run -ti -v $(pwd)/logs:/logs python-barcode
```
in which:
```python
Position text file:                                      
Position 0 : (x0,y0)
Context text file:
Destination : (yn,yn)                #final destination
Speed (m/s): S                       #default speed of pedestrian in m/s
Time interval (s) : ∆t              # time intervals between frames
```
More info on Phase 1 can be fine in Docs/PPM_Doc0.docx


