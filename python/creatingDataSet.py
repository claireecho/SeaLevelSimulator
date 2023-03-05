from pip._vendor import requests
import json
import numpy as np

f = open("xyz.txt", "w")

for y in np.arange(36.3206, 39.7175, 0.05):
    for x in np.arange(-79.36778, -74.37222, 0.05):
        response = requests.get(
            'http://localhost:5000/v1/test-dataset?locations='
            + str(y) + "," + str(x))
        z = response.json()['results'][0]['elevation']
        print(str(x) + " " + str(y) + " " + str(z))
        f.write(str(x) + " " + str(y) + " " + str(z) + "\n") 
    
