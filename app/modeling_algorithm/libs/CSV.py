import csv
from calendar import monthrange
from datetime import date, timedelta
import json
import os 
from os.path import *

# The main directory whenever the data gonna be stored
# MAIN_DIRECTORY = '.csv_api'
# CO_MAIN_DIRECTORY = '.clouds_parameters'
from Math_process import Math_process


# Here we will storage about cloud behavior
# how have the clouds been
# ['Overcast clouds', 'Broken clouds', 'Scattered clouds', 'Light rain', 'Few clouds', 'Clear Sky']

""" BEHAVIOR CLOUDS """
def create_file(directory_name,file_name):

    with open('csv'+'/behavior/'+str(directory_name)+'/'+str(file_name)+'.csv', 'w') as csv_file:

        # HEADERS
        writer = csv.writer(csv_file)
        writer.writerow(["time_start", "time_end", 'Overcast_clouds', 'Broken_clouds', 
            'Scattered_clouds', 'Light_rain', 'Few_clouds', 'Clear_Sky'])
    

def create_file_with_parameters(directory_name,file_name, time_start, time_end,list_values):

    with open('csv'+'/behavior/'+str(directory_name)+'/'+str(file_name)+'.csv', 'a') as csv_file:

        writer = csv.writer(csv_file)
        writer.writerow([time_start,time_end, list_values.count('Overcast clouds'),list_values.count('Broken clouds'),
            list_values.count('Scattered clouds'),list_values.count('Light rain'),list_values.count('Few clouds'),
            list_values.count('Clear Sky')])


""" VALUES FROM API """



def create_values_csv_file(directory_name, file_name):

    with open('csv'+'/values/'+str(directory_name)+'/'+str(file_name)+'.csv', 'w') as csv_file:
        
        # HEADERS
        writer = csv.writer(csv_file)
        writer.writerow(["time_start", "time_end","temperature", "precips", "clouds"])

def store_into_values(directory_name,file_name, time_start, time_end,list_temp, list_precip, list_clouds):
    
    with open('csv'+'/values/'+str(directory_name)+'/'+str(file_name)+'.csv', 'a') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow([time_start, time_end, list_temp,list_precip, list_clouds])


""" STORE TAKEN IN CARE WHICH PARAMETERS APPEAR WHENEVER THE BEHAVIOR CLOUD IS SHOWIG [LIGHT RAIN, HAS HER SELF PARAMETERS SUCH
    TEMPERATURE, PRECIPITATION, AND THE CODES OF THE CLOUDS]
    EVERY DIRECTORY MUST BE CREATED WITH A POINT IN THE BEGGINING TO BE OCCULT FROM THE ANOTHERS READERS, SUCH THE OS GONNA BE ANDROID
    BASED IN LINUX KERNEL, AND HER BASED ON UNIX, WE WILL MAKE OCCULT THE FILES ON THE DIRECTORIES """



# create the directory if this one not exists
def create_hidden_directories():

    global new_main_directory
    clouds_behavior_list = ['Overcast_clouds', 'Broken_clouds', 'Scattered_clouds', 
                            'Light_rain', 'Few_clouds', 'Clear_Sky']
    new_main_directory = '.csv/.clouds_parameters/'

    if (exists('.csv')):
        return True
    else:
        os.makedirs(new_main_directory)
        for x in clouds_behavior_list:
            os.makedirs(new_main_directory+'.'+x+'/.2017')
            os.makedirs(new_main_directory+'.'+x+'/.2018')
            os.makedirs(new_main_directory+'.'+x+'/.2019')
        return None
create_hidden_directories()
# reate_main_directories() call this method to access to global variable

# this method must be instantiated first, this one created the headers and the file name
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



    