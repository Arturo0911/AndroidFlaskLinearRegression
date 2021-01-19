import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from urllib.request import urlopen
from urllib.error import HTTPError
from pprint import pprint
import requests
from calendar import monthrange
from datetime import date, timedelta
import json


# importing modules
from app.modeling_algorithm.libs import CSV
from app.modeling_algorithm.libs import API_values
from app.modeling_algorithm.libs import Create_days
from app.modeling_algorithm.libs import Interface_objects
from app.modeling_algorithm.libs.keys import keys


# CONSTANTS
latitude = '-2.335017'
longitude = '-80.229769'

scattered_cloud_object = list()
broken_cloud_object = list()
light_rain_object = list()
few_clouds_object = list()
clear_sky_object = list()
overcasted_clouds_objects= list()


# Create a object with the values 
url_from_API = {
    'latitude': '-2.335017',
    'longitude':'-80.229769',
    'key_url_api':'c09b8f1a39d14a8bb9d343ccab529441'
}


# if __name__ == "__main__":
def initializer():
    # Instantiate from Create_days class

    days = Create_days()
    days.generate_appends()

    new_query = API_values(keys.url_from_API['latitude'], keys.url_from_API['longitude'])
    CSV.create_hidden_directories()
    for x in days.get_objects():

        for i in Interface_objects.make_list():

            CSV.create_headers_into_hidden_directories(x,x,i)

        for y in range(1,len(days.get_objects()[x])):
            time_start = days.get_objects()[x][y-1]
            time_end = days.get_objects()[x][y]
            
            new_query.generate_process(time_start, time_end) # process is called, and keys from the API is used
            
            for j in Interface_objects.create_objects_from_clouds(new_query.response_data['data']):

                CSV.generate_data_into_csv_files(x,x,time_start,time_end, j,
                    Interface_objects.create_objects_from_clouds(new_query.response_data['data'])[j])
            


