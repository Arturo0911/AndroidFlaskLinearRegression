from app.modeling_algorithm.libs.Math_process import Math_process
from datetime import date, timedelta
import json
import os 
from os.path import *
import csv
import requests




class Days_test:
    def __init__(self):
        self.year_2021 = list()

        self.october_2020 = date(2020, 10, 1)
        self.january_2021 = date(2021, 1, 27)

        self.objects = {}


    def generate_appends(self):
        delta_2021 = self.january_2021 - self.october_2020
        for x in range(delta_2021.days + 1):
            days = self.october_2020 + timedelta(days= x)
            self.year_2021.append(str(days))
        self.objects[2021] = self.year_2021

    def get_objects(self):
        return self.objects
    
def create_hidden_directories():

    global new_main_directory
    clouds_behavior_list = ['Overcast_clouds', 'Broken_clouds', 'Scattered_clouds', 
                            'Light_rain', 'Few_clouds', 'Clear_Sky']
    new_main_directory = '.prediction/.clouds_parameters/'

    if (exists('.prediction')):
        return True
    else:
        os.makedirs(new_main_directory)
        for x in clouds_behavior_list:
            os.makedirs(new_main_directory+'.'+x+'/.2021')
        return None
# create_hidden_directories()
def create_headers_into_hidden_directories(dir_name, file_name, cloud_parameter):
    # Create headers, with the corrects values
    with open(new_main_directory+'.'+cloud_parameter+'/.'+str(dir_name)+'/.'+str(file_name)+'.csv', 'w') as file:

        writer = csv.writer(file)
        writer.writerow(['time_start', 'time_end', 'cloud_description','relative_humidity','clouds' ,'precip', 'temperature', 'icon','code'])

    return


def generate_data_into_csv_files(dir_name, file_name,time_start, time_end, cloud_parameter, objects_values):

    with open(new_main_directory+'.'+cloud_parameter+'/.'+str(dir_name)+'/.'+str(file_name)+'.csv', 'a') as file_csv:
        
        writer = csv.writer(file_csv)
        writer.writerow([time_start,time_end,cloud_parameter, objects_values['relative_humidity'],objects_values['clouds'],objects_values['precipitation'],objects_values['temperature'],
        objects_values['icon'],objects_values['code'] ]) # complete the cells

    return







def create_objects_from_clouds(api_object):

    math_process = Math_process()

    global scattered_cloud_object
    global broken_cloud_object
    global light_rain_object 
    global few_clouds_object
    global clear_sky_object
    global overcast_clouds_objects

    
    # to be stored
    scattered_cloud_object = list()
    broken_cloud_object = list()
    light_rain_object = list()
    few_clouds_object = list()
    clear_sky_object = list()
    overcast_clouds_objects = list()

    
    # loop

    for z in api_object:

        if z['weather']['description'] == "Few clouds":
            few_clouds_object.append(
                {'cloud_description':z['weather']['description'],'icon':z['weather']['icon'],
            'relative_humidity':z['rh'],'code':z['weather']['code'] ,'temperature': z['temp'],
            'clouds':z['clouds'], 'precipitation':z['precip']}
            )
            #print(few_clouds_object)
            

        elif z['weather']['description'] == "Broken clouds":
            broken_cloud_object.append(
                {'cloud_description':z['weather']['description'],'icon':z['weather']['icon'],
            'relative_humidity':z['rh'],'code':z['weather']['code'] ,'temperature': z['temp'],
            'clouds':z['clouds'], 'precipitation':z['precip']}
            )
            #print(broken_cloud_object)
            #break
            

        elif z['weather']['description'] == "Overcast clouds":
            overcast_clouds_objects.append(
                {'cloud_description':z['weather']['description'],'icon':z['weather']['icon'],
            'relative_humidity':z['rh'],'code':z['weather']['code'] ,'temperature': z['temp'],
            'clouds':z['clouds'], 'precipitation':z['precip']}
            )
            
            #break

        elif z['weather']['description'] == "Scattered clouds":
            scattered_cloud_object.append(
                {'cloud_description':z['weather']['description'],'icon':z['weather']['icon'],
            'relative_humidity':z['rh'],'code':z['weather']['code'] ,'temperature': z['temp'],
            'clouds':z['clouds'], 'precipitation':z['precip']}
            )
            #print(scattered_cloud_object)
            #break

        elif z['weather']['description'] == "Light rain":
            light_rain_object.append(
                {'cloud_description':z['weather']['description'],'icon':z['weather']['icon'],
            'relative_humidity':z['rh'],'code':z['weather']['code'] ,'temperature': z['temp'],
            'clouds':z['clouds'], 'precipitation':z['precip']}
            )
            #print(light_rain_object)
            #break

        elif z['weather']['description'] == "Clear Sky":
            clear_sky_object.append(
                {'cloud_description':z['weather']['description'],'icon':z['weather']['icon'],
            'relative_humidity':z['rh'],'code':z['weather']['code'] ,'temperature': z['temp'],
            'clouds':z['clouds'], 'precipitation':z['precip']}
            )
            #print(clear_sky_object)
            #break

        else:
            pass

    general_object = {
        'Overcast_clouds':math_process.average(overcast_clouds_objects,'Overcast_clouds'),
        'Broken_clouds':math_process.average(broken_cloud_object,'Broken_clouds'),
        'Few_clouds':math_process.average(few_clouds_object,'Few_clouds'),
        'Clear_Sky':math_process.average(clear_sky_object,'Clear_Sky'),
        'Light_rain':math_process.average(light_rain_object,'Light_rain'),
        'Scattered_clouds':math_process.average(scattered_cloud_object,'Scattered_clouds')
        }

    return general_object
    

def make_list():
    description_cloud_list = ['Overcast_clouds','Broken_clouds','Few_clouds', 'Clear_Sky','Light_rain','Scattered_clouds']
    return description_cloud_list


class Api_values:
    def __init__(self, latitude, longitude):
        
        """
        @parameters latitude, longitud, time_start, time_end
        time_start and time_end must be Strings, because the algorythm it's getting 
        the time using for loops with timedelta
        """
        self.latitude = latitude
        self.longitude = longitude
        self.time_start = None
        self.time_end = None
        
        # New api key is c09b8f1a39d14a8bb9d343ccab529441
        # self.weatherbi_key = 'c96c2aa02b1b43e184580f8efe648f59'
        
        self.weatherbi_key = 'dc9d17be38b84c0ebd5dd3c8a18c987a'
        self.url = None
        self.response_data = None


    def generate_process(self, time_start, time_end):
        self.time_start = time_start
        self.time_end = time_end
        self.url = 'https://api.weatherbit.io/v2.0/history/hourly?lat={}&lon={}&start_date={}&end_date={}&tz=local&key={}'.format(self.latitude,
            self.longitude,self.time_start,self.time_end,self.weatherbi_key)

        self.response_data  = requests.get(self.url).json()
        

    def get_api_key(self):

        return self.weatherbi_key

    def check_lat_long(self):

        return self.latitude, self.longitud

    def check_location(self):

        return self.response_data['city_name']


    # keys from the json data requested
    def get_keys(self):

        return self.response_data.keys()

    
    # One param like clouds, time local
    def get_parameters(self):

        # Here the first question is "How many parameters i must to cross to get the descriptions
        # of sky are in the weather data ?"

        print(len(self.response_data['data'][0]))
        #for x in self.response_data:
        #    print(x['data'])

    def get_parameters_sky_behavior(self):

        lista_value = []

        for x in self.response_data['data']:

            if x['weather']['description'] not in lista_value :
                lista_value.append(x['weather']['description'])

        return lista_value



# CONSTANTS
latitude = '-2.335017'
longitude = '-80.229769'

scattered_cloud_object = list()
broken_cloud_object = list()
light_rain_object = list()
few_clouds_object = list()
clear_sky_object = list()
overcasted_clouds_objects= list()

def initialize_model():
    days = Days_test()
    days.generate_appends()


    new_query = Api_values('-2.335017', '-80.229769')  # API_values('-2.335017', '-80.229769')
    create_hidden_directories()
    for x in days.get_objects():

        for i in make_list():
            # print(i)
            create_headers_into_hidden_directories(x,x,i)

        for y in range(1,len(days.get_objects()[x])):
            time_start = days.get_objects()[x][y-1]
            time_end = days.get_objects()[x][y]
            
            new_query.generate_process(time_start, time_end) # process is called, and keys from the API is used
            
            for j in create_objects_from_clouds(new_query.response_data['data']):

                generate_data_into_csv_files(x,x,time_start,time_end, j,
                    create_objects_from_clouds(new_query.response_data['data'])[j])
            

