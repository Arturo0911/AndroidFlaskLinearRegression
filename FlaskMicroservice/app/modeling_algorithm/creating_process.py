from app import app

import time
import statistics
from datetime import time
from app.modeling_algorithm.libs.Create_days import Create_days as cd
from app.modeling_algorithm.libs import Interface_objects
from app.modeling_algorithm.libs.Math_process import Math_process
from app.modeling_algorithm.libs.Interface_objects import make_list
# from Interface_objects import make_list
# from Math_process import Math_process 
from os import O_TRUNC, listxattr
# from Create_days import Create_days as cd

from pandas.io import api
import numpy as np
import pandas as pd
from pprint import pprint
import matplotlib.pyplot as plt
import seaborn as sns

from concurrent.futures import ThreadPoolExecutor



class Init_test:

    def __init__(self):
        # initialize the parameters to be the query

        self._path = '.csv/.clouds_parameters/.{}/.{}/.{}.csv'

    def read_dataframe(self, object_parameters):
        # Return the dataframe with all the values in the data
        # set the names of parameters, to avoid get verbose mode on the algorithm
        '''
            objects_ = {
                'values': 
                    {
                        'cloud_parameter': x,
                        'year_activity': y
                    }
                }
        '''

        cloud_param = object_parameters['values']['cloud_parameter']
        year_param = object_parameters['values']['year_activity']
        data_frame = pd.read_csv(self._path.format(
            cloud_param, year_param, year_param))
        return data_frame

    def make_subset(self, object_parameters):
        """
            get the parameters with the object parameters
            set cloud parameters in differents years
            create variables to avoid big names into the methods
            the variable first_param_year will be used two times, 
            because the directory and the file has the same name

            Structure of the parameters to be evaluated
            object_parameters => {

                'value': {'cloud_parameter': Behavior cloud: Broken_clouds, Light_rain, 
                            Clear_Sky,'year_activity': None,'filter': 'the filter is the
                             header of each column to be evaluated'}
            }
        """

        first_param_cloud = object_parameters['values']['cloud_parameter']
        first_param_year = object_parameters['values']['year_activity']

        dataframe = pd.read_csv(self._path.format(
            first_param_cloud, first_param_year, first_param_year))

        # taking the first_data_parameter, put the parameter to be filtered
        # this one gonna return the subset with the filter
        return dataframe

    def set_parameters(self, object_parameters, range):
        """
        get the values from the dictionary object_parameters
        set the range of the filter that we wanna show
        """

        subset = self.make_subset(object_parameters)

        data_range = self.dataframe_weather[subset >= float(range)]

        return data_range

    def _comparative_between_three_years(self):
        """
        In this method, we will called all the values, parsed and draw a 
        charted scattered, but presenting in a loop for the three years, 
        we already have stored in csv files.
        """

        # Instance from the another main classes

        math_process = Math_process()

        create_days = cd()
        create_days.generate_appends()

        # Lists
        coefficient_positive = list()
        coefficient_negative = list()

        # =======================================
        scattered_cloud = list()
        broken_cloud = list()
        light_rain = list()
        few_clouds = list()
        clear_sky = list()
        overcast_clouds = list()

        for x in make_list():
            # Loop in each year stored 2017 2018 2019 2020.
            # Now we can get the antoher parameters of the sky such overcastered
            # from the make_list() function

            for y in create_days.get_objects():
                # Initializers
                # the only reason is for to generate a list with the time start at the list_date
                # and temperature values at the list_temperature

                list_humidity = list()
                list_temperature = list()
                list_time_prediction = list()

                # get the list of clouds parameters and year activity
                objects_ = {
                    'values': {
                        'cloud_parameter': x,
                        'year_activity': y
                    }
                }

                # set the subset, temperature, is the best parameter to filter by.
                dataframe_filtered = self.read_dataframe(
                    objects_)[self.read_dataframe(objects_)['temperature'] > 0]
                # LOOPS FOR APPENDS
                for i in dataframe_filtered['relative_humidity']:
                    list_humidity.append(i)

                for j in dataframe_filtered['temperature']:
                    list_temperature.append(j)

                for k, l in zip(dataframe_filtered['time_start'], dataframe_filtered['time_end']):
                    list_time_prediction.append(k+" - "+l)

                # set the object_data with the values.

                object_data = {
                    'x': list_humidity,
                    'y': list_temperature,
                    'time_prediction': list_time_prediction,
                }

                # group by cloud type and add their properties
                if x == "Overcast_clouds":
                    overcast_clouds.append({x: {'cloud_type': x, str(y): object_data,
                                                'coefficient_correlation': math_process.correlation_coefficient(object_data)}})
                elif x == "Broken_clouds":
                    broken_cloud.append({x: {'cloud_type': x, str(y): object_data,
                                             'coefficient_correlation': math_process.correlation_coefficient(object_data)}})
                elif x == "Scattered_clouds":
                    scattered_cloud.append({x: {'cloud_type': x, str(y): object_data,
                                                'coefficient_correlation': math_process.correlation_coefficient(object_data)}})
                elif x == "Few_clouds":
                    few_clouds.append({x: {'cloud_type': x, str(y): object_data,
                                           'coefficient_correlation': math_process.correlation_coefficient(object_data)}})
                elif x == "Clear_Sky":
                    clear_sky.append({x: {'cloud_type': x, str(y): object_data,
                                          'coefficient_correlation': math_process.correlation_coefficient(object_data)}})
                elif x == "Light_rain":
                    light_rain.append({x: {'cloud_type': x, str(y): object_data,
                                           'coefficient_correlation': math_process.correlation_coefficient(object_data)}})
                else:
                    pass

                # use correlation_coefficient() instead of check_covariance()
                if math_process.correlation_coefficient(object_data) > 0:
                    # here prove that the coefficient is greater than 0
                    coefficient_positive.append({'cloud_type': x, str(y): object_data,
                                                 'coefficient_correlation': math_process.correlation_coefficient(object_data)})

                elif math_process.correlation_coefficient(object_data) == 0:
                    pass

                else:
                    coefficient_negative.append({'cloud_type': x, str(y): object_data,
                                                 'coefficient_correlation': math_process.correlation_coefficient(object_data)})

        coefficients = {
            'Overcast_clouds': overcast_clouds,
            'Broken_clouds': broken_cloud,
            'Scattered_clouds': scattered_cloud,
            'Few_clouds': few_clouds,
            'Clear_Sky': clear_sky,
            'Light_rain': light_rain
        }
        # return coefficient_positive, coefficient_negative
        return coefficients, coefficient_positive, coefficient_negative


def main(cloud_type='Overcast_clouds',day_to_evaluate = 24,year_to_be_evaluated = 2021):
    """
        This function, only will be read the instancies, from the main Class
        humidity relative is the X variable and the temperature is Y
    """
    test_init = Init_test()
    list_coefficients = list()
    coefficients, positive, negative = test_init._comparative_between_three_years()

    model_2017 = optimization(cloud_type,'2017',['2018','2019','2020'])
    model_2018 = optimization(cloud_type,'2018',['2017','2019','2020'])
    model_2019 = optimization(cloud_type,'2019',['2017','2018','2020'])
    model_2020 = optimization(cloud_type,'2020',['2017','2018','2019'])

    list_coefficients.append(model_2017['2017']['average_accuracy_total'])
    list_coefficients.append(model_2018['2018']['average_accuracy_total'])
    list_coefficients.append(model_2019['2019']['average_accuracy_total'])
    list_coefficients.append(model_2020['2020']['average_accuracy_total'])


    optimized_value = max(list_coefficients)

    # still how to pass the final bias to the another function

    if model_2017['2017']['average_accuracy_total'] == optimized_value:
        return {
            'bias': model_2017['2017']['bias'],
            'year': '2017',
            'cloud_type':cloud_type,
            'object_data':coefficients[cloud_type][0][cloud_type]['2017'],
            'day_to_evaluate':day_to_evaluate,
            'year_to_be_evaluated':year_to_be_evaluated
        }
    elif model_2018['2018']['average_accuracy_total'] == optimized_value:
        return {
            'bias': model_2018['2018']['bias'],
            'year': '2018',
            'cloud_type':cloud_type,
            'object_data':coefficients[cloud_type][1][cloud_type]['2018'],
            'day_to_evaluate':day_to_evaluate,
            'year_to_be_evaluated':year_to_be_evaluated
        }
    elif model_2019['2019']['average_accuracy_total'] == optimized_value:
        return {
            'bias': model_2019['2019']['bias'],
            'year': '2019',
            'cloud_type':cloud_type,
            'object_data':coefficients[cloud_type][2][cloud_type]['2019'],
            'day_to_evaluate':day_to_evaluate,
            'year_to_be_evaluated':year_to_be_evaluated
        }
    elif model_2020['2020']['average_accuracy_total'] == optimized_value:
        return {
            'bias': model_2020['2020']['bias'],
            'year': '2020',
            'cloud_type':cloud_type,
            'object_data':coefficients[cloud_type][3][cloud_type]['2020'],
            'day_to_evaluate':day_to_evaluate,
            'year_to_be_evaluated':year_to_be_evaluated
        }
    else:
        return {'error': 'Error in modeling'}
        

def optimization(cloud_type,year_model,years):#cloud_type,year_model):
    '''
    Years parameters would be: 
        years = ['2017','2018','2019'] is the year model is 2020
        years = ['2018','2019','2020'] is the year model is 2017
        years = ['2017','2019','2020'] is the year model is 2018
        years = ['2017','2018','2020'] is the year model is 2019
    '''
    model_1 = None
    model_2 = None
    model_3 = None


    model_1 = testing_models(cloud_type, year_model, years[0])
    model_2 = testing_models(cloud_type, year_model, years[1])
    model_3 = testing_models(cloud_type, year_model, years[2])

    average = [model_1['accuracy'],
    model_2['accuracy'],
    model_3['accuracy']]

    bias = [
        model_1['bias'],
        model_2['bias'],
        model_3['bias']
    ]

    which_model_choose = {
        year_model: {
            'year_model':year_model,
            'average_accuracy_total': float(statistics.mean(average)),
            'cloud_type': model_1['cloud_type'],
            'bias':bias
        }
    }


    return which_model_choose



def testing_models(cloud_type, year_init, year_to_predict):

    init_test = Init_test()
    coefficients, positive, negative = init_test._comparative_between_three_years()
    Model_train = None
    Model_test = None

    try:
        if year_init == '2017':
            Model_train = coefficients[cloud_type][0][cloud_type][year_init]
        elif year_init == '2018':
            Model_train = coefficients[cloud_type][1][cloud_type][year_init]
        elif year_init == '2019':
            Model_train = coefficients[cloud_type][2][cloud_type][year_init]
        elif year_init == '2020':
            Model_train = coefficients[cloud_type][3][cloud_type][year_init]
        else:
            pass
    except Exception as e:
        print(str(e))

    try:
        if year_to_predict == '2017':
            Model_test = coefficients[cloud_type][0][cloud_type]['2017']
        elif year_to_predict == '2018':
            Model_test = coefficients[cloud_type][1][cloud_type]['2018']
        elif year_to_predict == '2019':
            Model_test = coefficients[cloud_type][2][cloud_type]['2019']
        elif year_to_predict == '2020':
            Model_test = coefficients[cloud_type][3][cloud_type]['2020']
        else:
            pass
    except Exception as e:
        print(str(e))

    # print(test_model_2017[cloud_type]['2017'])

    return Math_process().optimization_gradient_descent(
        Model_train,
        Model_test['x'],
        Model_test['y'],
        year_init,
        year_to_predict,
        cloud_type,
        Model_train['time_prediction'],
        Model_test['time_prediction']
    )

def init(x,y):
    
    all_data = main()

    # def presenting_model(self, 
    # bias,
    # model_prediction,
    # cloud_type,
    # y_data_to_be_evaluated, 
    # x_data_to_be_tested):

    return Math_process().presenting_model(
        all_data['bias'],
        all_data['object_data'],
        all_data['cloud_type'],
        y,
        x
        )

# init()

# 94