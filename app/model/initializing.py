from app.model.Model_prediction import Days_test as cd
from app.model.Model_prediction import make_list
from app.modeling_algorithm.libs.Math_process import Math_process

from pandas.io import api
import numpy as np
import pandas as pd
from pprint import pprint
import matplotlib.pyplot as plt




class Init_test:

    def __init__(self):
        # initialize the parameters to be the query

        self._path = '.prediction/.clouds_parameters/.{}/.{}/.{}.csv'

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
                    # 'time_prediction': list_time_prediction,
                }

                # group by cloud type and add their properties
                if x == "Overcast_clouds":
                    overcast_clouds.append({str(y): object_data})
                elif x == "Broken_clouds":
                    broken_cloud.append({str(y): object_data})
                elif x == "Scattered_clouds":
                    scattered_cloud.append({str(y): object_data})
                elif x == "Few_clouds":
                    few_clouds.append({str(y): object_data})
                elif x == "Clear_Sky":
                    clear_sky.append({str(y): object_data})
                elif x == "Light_rain":
                    light_rain.append({str(y): object_data})
                else:
                    pass

                # use correlation_coefficient() instead of check_covariance()
                """if math_process.correlation_coefficient(object_data) > 0:
                    # here prove that the coefficient is greater than 0
                    coefficient_positive.append({'cloud_type': x, str(y): object_data,
                                                 'coefficient_correlation': math_process.correlation_coefficient(object_data)})

                elif math_process.correlation_coefficient(object_data) == 0:
                    pass

                else:
                    coefficient_negative.append({'cloud_type': x, str(y): object_data,
                                                 'coefficient_correlation': math_process.correlation_coefficient(object_data)})
                """

        coefficients = {
            'Overcast_clouds': overcast_clouds,
            'Broken_clouds': broken_cloud,
            'Scattered_clouds': scattered_cloud,
            'Few_clouds': few_clouds,
            'Clear_Sky': clear_sky,
            'Light_rain': light_rain
        }
        # return coefficient_positive, coefficient_negative
        return coefficients
