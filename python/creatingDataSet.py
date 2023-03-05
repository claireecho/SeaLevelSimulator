from pip._vendor import requests
import json
import numpy as np

f = open("xyz.txt", "w")

for y in np.arange(36.354613, 39.608864, 0.04):
    for x in np.arange(-79.976295, -74.658492, 0.04):
        response = requests.get(
            'http://localhost:5000/v1/etopo1?locations='
            + str(y) + "," + str(x))
        z = response.json()['results'][0]['elevation']
        print(str(x) + " " + str(y) + " " + str(z))
        f.write(str(x) + " " + str(y) + " " + str(z) + "\n") 
    
