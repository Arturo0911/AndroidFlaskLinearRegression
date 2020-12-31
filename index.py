import requests
from pprint import pprint


# this area is for test the container

try:
    pprint(requests.get('http://0.0.0.0:5000/holis').json())

except Exception as e:
    print("Error by: " + str(e))


