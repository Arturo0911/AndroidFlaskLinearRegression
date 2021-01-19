""" 
IN THIS FILE, WE GONNA TEST THE DATA, USING COMPARATIONS BETWEEN DATAS, AND PARAMETERS   
"""
import time
from datetime import time
from Interface_objects import make_list
from Math_process import Math_process 
from os import O_TRUNC, listxattr
from Create_days import Create_days as cd

from pandas.io import api
import numpy as np
import pandas as pd
from pprint import pprint
import matplotlib.pyplot as plt
import seaborn as sns

from concurrent.futures import ThreadPoolExecutor


""" Libraries of the data storage """

# this one return the list o behavior to be instantiated.
# supervised machine learning 

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


    def readdataframe_using_seaborn(self):

        new_data_frame = pd.read_csv(self._path.format('Overcast_clouds', 2017,2017))
        return new_data_frame

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
        first_param_filter = object_parameters['values']['filter']

        dataframe = pd.read_csv(self._path.format(
            first_param_cloud, first_param_year, first_param_year))

        # taking the first_data_parameter, put the parameter to be filtered

        # subset_first = self.read_dataframe()[first_param_filter]

        # return first_data_frame_subset , second_data_frame_subset

        # this one gonna return the subset with the filter
        # return subset_first

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

        # Objects
        final_object = []
        object_with_correlassion_positive = []
        coefficient_positive = list()
        coefficient_negative = list()
        

        # for x in create_days.get_objects():
        for x in make_list():
            # Loop in each year stored 2017 2018 2019; comming soon 2020.
            # Now we can get the antoher parameters of the sky such overcastered
            # from the make_list() function

            for y in create_days.get_objects():
                # Initializers
                # the only reason is for to generate a list with the time start at the list_date
                # and temperature values at the list_temperature

                list_humidity = list()
                list_temperature = list()
                list_time_prediction = list()
                list_time_end = list()
                
                # get the list of clouds parameters and year activity
                objects_ = {
                    'values': {
                        'cloud_parameter': x,
                        'year_activity': y
                    }
                }
                
                # set the subset, temperature, is the best parameter to filter by.
                dataframe_filtered = self.read_dataframe(objects_)[self.read_dataframe(objects_)['temperature'] > 0]
                # LOOPS FOR APPENDS
                for i in dataframe_filtered['relative_humidity']:
                    list_humidity.append(i)

                for j in dataframe_filtered['temperature']:
                    list_temperature.append(j)

                for k,l in zip(dataframe_filtered['time_start'],dataframe_filtered['time_end']):
                    list_time_prediction.append(k+" - "+l)

                #for l in dataframe_filtered['time_end']:
                #    list_time_end.append(l)

                # set the object_data with the values.  
                
                object_data = {
                    'x': list_humidity,
                    'y': list_temperature,
                    'time_prediction': list_time_prediction,
                    #'time_end':list_time_end
                }

                # use correlation_coefficient() instead of check_covariance()
                if math_process.correlation_coefficient(object_data) > 0:
                    # here prove that the coefficient is greater than 0
                    coefficient_positive.append({'cloud_type': x,str(y): object_data, 
                    'coefficient_correlation': math_process.correlation_coefficient(object_data) })

                elif math_process.correlation_coefficient(object_data) == 0:
                    pass
                    
                else:
                    coefficient_negative.append({'cloud_type': x,str(y): object_data, 
                    'coefficient_correlation': math_process.correlation_coefficient(object_data) })

                    """
                    plt.scatter(object_data['x'], object_data['y'])
                    plt.xlabel("Dates")
                    plt.ylabel("Temperature")
                    plt.show()
                    """
        return coefficient_positive, coefficient_negative
        



def main():
    """
        This function, only will be read the instancies, from the main Class
        humidity relative is the X variable and the temperature is Y
    """
    test_init = Init_test()
    positive, negative = test_init._comparative_between_three_years()


    prediction_2017 = Math_process().testing_mathematician_model(positive[0]['2017'], 
                positive[1]['2018']['x'], positive[1]['2018']['y'], '2017', positive[0]['cloud_type'],
                positive[0]['2017']['time_prediction'],positive[1]['2018']['time_prediction'])
    
    pprint(prediction_2017)


    '''with ThreadPoolExecutor(max_workers=2) as executors:

         executors.submit(print(prediction_2017))'''

    '''executors.submit(Math_process().testing_mathematician_model, positive[0]['2017'], 
                positive[0]['2017']['x'], positive[0]['2017']['y'], '2017', positive[0]['cloud_type'],
                positive[0]['2017']['time_prediction'],positive[1]['2018']['time_prediction'])'''
        
        # the prediction whenever the cloud type is the same
    '''executors.submit(Math_process().testing_mathematician_model, negative[0]['2017'], 
                negative[0]['2017']['x'], negative[0]['2017']['y'], '2017', negative[0]['cloud_type'],
                negative[0]['2017']['time_prediction'],negative[1]['2018']['time_prediction'])'''



    '''executors.submit(Math_process().testing_mathematician_model, negative[0]['2017'], 
                negative[1]['2018']['x'], negative[1]['2018']['y'], '2018', negative[1]['cloud_type'])'''
                
    
    '''executors.submit(Math_process().testing_mathematician_model, positive[0]['2017'], 
                positive[0]['2017']['x'], positive[0]['2017']['y'], '2017', positive[0]['cloud_type'])
        
        executors.submit(Math_process().testing_mathematician_model, positive[0]['2017'], 
                positive[1]['2018']['x'], positive[1]['2018']['y'], '2018',positive[1]['cloud_type'])

        executors.submit(Math_process().testing_mathematician_model, positive[0]['2017'], 
                positive[2]['2019']['x'], positive[2]['2019']['y'], '2019',positive[2]['cloud_type'])'''



main()


