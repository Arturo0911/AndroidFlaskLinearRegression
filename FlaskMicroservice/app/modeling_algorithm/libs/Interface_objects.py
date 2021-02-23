from app import app
from app.modeling_algorithm.libs.Math_process import Math_process 
#  Function to append new instances from the api


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

    # print(overcast_clouds_objects)
    # print(len(overcast_clouds_objects))


    """ print(math_process.average(overcast_clouds_objects,'Overcast_clouds'))
    print(math_process.average(broken_cloud_object,'Broken_clouds'))
    print(math_process.average(few_clouds_object,'Few_clouds'))
    print(math_process.average(clear_sky_object,'Clear_Sky'))
    print(math_process.average(light_rain_object,'Light_rain'))
    print(math_process.average(scattered_cloud_object,'Scattered_clouds'))"""



    
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



