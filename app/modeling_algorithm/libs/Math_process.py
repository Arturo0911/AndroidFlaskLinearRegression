#!/usr/bin/python3


""" MATH PROCESS  """
import math
from pprint import pprint
import random
from concurrent.futures import ThreadPoolExecutor
from types import new_class 


#----------------------------------------------#
#      Generate_parameters_from_regression     #
#           Y = β0 + β1*x                      #
#----------------------------------------------#

#----------------------------------------------#
#       β1 = ⅀((x - x⁻)*(y - y⁻))              #
#                 ⅀ ( x - x²)                  #
#----------------------------------------------#

#----------------------------------------------#
#    Structure of the obejcts_data = {         #
#            'x': list,                        #
#            'y': list                         #
#           }                                  #
#----------------------------------------------#

#----------------------------------------------#
#               Y = β0 + β1*x                  #
#----------------------------------------------#


class Math_process:


    def __init__(self):

        # initialize a executor with 2 threads
        self.executor = ThreadPoolExecutor(max_workers=2)


    def Generate_average_from_list(self, list_values):
        # This one, gonna be util, whenever we want to get average
        # from the API values

        average = "{0:.3f}".format(sum(list_values) / len(list_values))

        return average

    def Generate_parameters_from_regression(self, objects_data):

        # Define parameters
        list_x = list()
        list_y = list()
        list_pow = list()
        MAX_X = sorted(objects_data['x'])[len(objects_data['x']) - 1]
        MIN_X = sorted(objects_data['x'])[0]

        x_average = self._define_average(
            sum(objects_data['x']), len(objects_data['x']))
        y_average = self._define_average(
            sum(objects_data['y']), len(objects_data['y']))

        for x in objects_data['x']:
            list_x.append(float(x - x_average))

        for y in objects_data['y']:
            list_y.append(float(y - y_average))

        for z in objects_data['x']:
            list_pow.append(float(pow((z - x_average), 2)))

        # Assuming, that both lists, has the same length
        CONST_LENGHT = len(list_x)
        total_sum = 0

        for i in range(CONST_LENGHT):
            total_sum += (float(list_x[i] * list_y[i]))

        β1 = float("{0:.3f}".format((total_sum / (sum(list_pow)))))
        β0 = float(y_average - (β1*x_average))

        prediction_model = {
            # is necessary set the MAX and MIN value
            # in each test, the value cannot be much more
            # of max value and lesser than min value

            'β1': float("{0:.3f}".format(β1)),
            'β0': float("{0:.3f}".format(β0)),
            'x_average': x_average,
            'y_average': y_average,
            'max_value': MAX_X,
            'min_value': MIN_X
        }
        return prediction_model

    # Use the math model to test the prediction

    def test_math_model(self, objects_data, x_data):
        # Where x_data is the list of values to be proveds,
        # to calculated the aprox of the value requiered
        # Every value rejected will be stored in an array,
        # after that, calculate which is the percent of wins
        # under the total of the values inserteds

        # Set the list of contain the values
        rejected_list = list()
        winner_list = list()
        cases = 1
        rejected_cases = 0

        # Assign the prediction model to the variable, to access all the stored data.
        object_model = self.Generate_parameters_from_regression(objects_data)
        y = 0
        print("[*] The prediction model is Y  = %s + X * %s  " %
              (object_model['β0'], object_model['β1']))

        try:
            # initialized ttry catch with loop insided
            for x in x_data:
                # print(x)
                if float(x) > object_model['max_value'] or float(x) < object_model['min_value']:
                    # print(bcolors.WARNING+"[x] this value cannot be used, because 
                    # it is not in the stablished range.")
                    # print("[x] CASE %s  value %s    Rejected."%(cases,x))
                    rejected_cases += 1
                    rejected_list.append(x)
                else:
                    y = float("{0:.3f}".format(
                        float(object_model['β0']) + (float(object_model['β1']) * float(x))))
                    print("[*] CASE %s  Passed  value %s." % (cases, x))
                    winner_list.append(x)
                    # print (bcolors.OKBLUE+"the prediction is: %s"%y)
                cases += 1

        except Exception as e:
            print("Error by: "+str(e))
        else:
            pass
            
        finally:

            rejecteds_percents = float((len(rejected_list) / len(x_data))*100)
            accepted_percents = float((len(winner_list) / len(x_data))*100)
            
            prediction = {
                'rejected_elements': len(rejected_list),
                'acepted_elements': len(winner_list),
                'rejected_percents': float("{0:.3f}".format(rejecteds_percents)),
                'acepted_percents': float("{0:.3f}".format(accepted_percents)),
            }
            print("\n")
            pprint(prediction)

    def learning_supervised(self):
        #--------------------------------------------------#
        # This method will evaluate the value of percents  #
        # of the test in the self method test_math_model   #
        #--------------------------------------------------#
        pass

    def _define_average(self, number, length):

        average = "{0:.2f}".format(number/length)
        return float(average)

    def average(self, _object_, description):
        # This method insert into the csv files, all the data

        if len(_object_) > 0:

            temp_sum = 0
            clouds_sum = 0
            precip_sum = 0
            relative_humidity_sum = 0

            for x in _object_:

                if x['temperature'] is not None:
                    temp_sum += int(x['temperature'])

                if x['clouds'] is not None:
                    clouds_sum += int(x['clouds'])

                if x['precipitation'] is not None:
                    precip_sum += int(x['precipitation'])

                if x['relative_humidity'] is not None:
                    relative_humidity_sum += int(x['relative_humidity'])

            final_object = {

                'cloud_description': description,
                'icon': _object_[0]['icon'], 
                'relative_humidity': self._define_average(relative_humidity_sum,len(_object_)), 
                'code': _object_[0]['code'],
                'temperature': self._define_average(temp_sum, len(_object_)),
                'clouds': self._define_average(clouds_sum, len(_object_)),
                'precipitation': self._define_average(precip_sum, len(_object_))
            }

            return final_object
        else:
            final_object = {
                # In case that the result will not do any with the value
                # 'None' then i will change None by "None" as String

                'cloud_description': description,
                'icon': None, 'relative_humidity': None, 'code': None,
                'temperature': None,
                'clouds': None,
                'precipitation': None
            }

            return final_object

    def check_covariance(self, object_values):
        # This method will be return True o False
        # object values is the list with all the parameters, without the NaN parameter
        # define a Sx and Sy as the covariance methods
        # set the media of values
        # use values with 3 decimals
        # asssume that the values of x and y has the same length
        # whenever the covariance is greater than 1, it's mean
        # that your correlation is strong and on higher values to x is
        # higher values to y
        """
            Structure from the list values
            object_values = {
                'x':None,
                'y':None
            }

        """

        # initializers

        covariance = 1
        list_x = list()
        list_y = list()

        # Set the size of list

        X_SIZE = len(object_values['x'])
        Y_SIZE = len(object_values['y'])

        average_x = float(sum(object_values['x'])/X_SIZE)
        average_y = float(sum(object_values['y'])/Y_SIZE)

        # X
        for x in object_values['x']:
            list_x.append(float(x - average_x))

        # Y
        for y in object_values['y']:
            list_y.append(float(y - average_y))

        for i in range(X_SIZE):

            covariance += list_x[i] * list_y[i]

        Sxy = float("{0:.3f}".format(covariance / (X_SIZE - 1)))

        return Sxy

    def variance(self, object_values):
        # As the whole values both x and y has the same lenght,
        # then use only a constant to set the length
        # asssume that the values of x and y has the same length

        SIZE_VALUES = len(object_values['x'])

        list_x = list()
        list_y = list()

        # define average from both values
        average_x = float((sum(object_values['x']) / SIZE_VALUES))
        average_y = float((sum(object_values['y']) / SIZE_VALUES))

        # First loops to store the difference between the value and her average
        for x in object_values['x']:

            list_x.append(float(pow(float(x - average_x), 2)))

        for y in object_values['y']:

            list_y.append(float(pow(float(y - average_y), 2)))

        # Set the Variance from both values, the format is with 3 decimals

        # print(sum(list_x)/9)
        # print(sum(list_y) /9)

        Sx = float("{0:.3f}".format(
            pow(float("{0:.3f}".format((sum(list_x))/(SIZE_VALUES - 1))), 0.5)))
        Sy = float("{0:.3f}".format(
            pow(float("{0:.3f}".format((sum(list_y))/(SIZE_VALUES - 1))), 0.5)))

        # Return the Variance from both values
        # Doing the testing in the test_model_weather_parameters.py

        return Sx, Sy

        # print(Sx, Sy)

    def correlation_coefficient(self, object_values):

        Sxy = self.check_covariance(object_values)
        Sx, Sy = self.variance(object_values)

        return float("{0:.3f}".format((Sxy) / (Sx * Sy)))


    def optimization_gradient_descent(self):
        # this method is to verify the errors in the math model

        pass

    def testing_mathematician_model(self, objects_data, x_data_model, y_data_model, year_tested):
        '''
        testing the math model taking in aacount about 
        the values to be proccessed
        the another goal in this method is take how many variables 
        (speaking in percent) aren't matching with the parameters, 
        for example: we have the variables X & Y
        There are a limit to use the values to be processed 
        the max and the min, and after that using one proccess to get the value in the intercept 'b'
        to get the wished value intercept

        Every value is indexed in one ArrayList and inserted into the function

        Read this one in case that i can't prove the code above 
        x_data_model are the x values from different year with the which one create de object model
        in some words, if the model was created with the object with the year 2017
        then x_data_model and y_data_model will be the x's and y's values from 2018 or 2019 
        years
        
        Resuming above, after three days, i gonna prove that algorithm
    
        '''

        #----------------------------------------------#
        #    Structure of the obejcts_data = {         #
        #            'x': list,                        #
        #            'y': list                         #
        #           }                                  #
        #----------------------------------------------#


        # Define the intercept 'b' as None value
        # in the gradient descent prove the real value
        # initialize in None to avoid unnecessary numbers
        b = None # the bias
        percent_difference = None
        validator = None        
        count_cases = 0 # the position of each loop
        values_near_to_goal = list()
        values_tested = list()
        total_error = 0.0 # this one gonna to get all the values without prediction
        

        math_model = self.Generate_parameters_from_regression(objects_data)
        #self.testing_simplify()
        
        try:
            
            '''for x, y in zip(x_data_model, y_data_model):

                count_cases += 1
                validator = self.y_prediction(math_model['β0'], math_model['β1'], x)

                if validator  == y:
                    print("[*] Test case Passed!")
                else:

                    if b is not None:
                        
                        print("bias isn't None ")
                        validator += b
                        percent_difference = float("{0:.3f}".format( 100 -((y/validator)*100)))

                        while True:
                            # bias, data, beta_0, beta_1, x_value
                            if (percent_difference <= float(3) and percent_difference >= float(-3) and 
                            self.check_bias(b, values_near_to_goal,math_model['β0'], math_model['β1'],x)):
                                values_near_to_goal.append(y)
                                break
                            else:
                                while True:
                                    b = random.uniform(-4,4)
                                    validator += b
                                    percent_difference = float("{0:.3f}".format( 100 -((y/validator)*100)))
                                    # self.executor(self.check_bias, ) 
                                    if percent_difference <=  float(3) and percent_difference >= float(-3):
                                        print(" [*] Enter in the conditional with the random uniform to bias different from None")
                                        values_near_to_goal.append(y)
                                        break
                                    else:
                                        continue
                    else:

                        percent_difference = float("{0:.3f}".format( 100 -((y/validator)*100)))

                        # in the case that the value is in the range of difference beteen -3 or 3
                        # in this case add into the append the new value
                        if percent_difference <=  float(3) and percent_difference >= float(-3):
                            values_near_to_goal.append(y)
                            
                        else:
                            while True:
                                # in this loop i try to prove that generated random number 
                                # between -4  and 4, including floating numbers.
                                # i gonna to balanced the math model, only to avoid 
                                # generated a big MSE, practically is i'm avoiding the errors
                            
                                b = random.uniform(-4,4)
                                validator += b
                                percent_difference = float("{0:.3f}".format( 100 -((y/validator)*100)))
                                # self.executor(self.check_bias, ) 
                                if percent_difference <=  float(3) and percent_difference >= float(-3):
                                    print(" [*] Enter in the conditional with the random uniform to bias different from None")
                                    values_near_to_goal.append(y)
                                    break
                                else:
                                    continue'''
            for x,y in zip(x_data_model, y_data_model):
                validator = self.y_prediction(math_model['β0'], math_model['β1'], x)

                if (validator - y == 0) or ((validator - y) >= -3 and (validator - y )<= 3):
                    # print("[*] Error margin prediction is 0 or is lesser than 3 and greater than -3")
                    # print("the validator %s and the value desired %s  and the accerts about the prediction are %s percent"%(validator, y,
                    # float("{0:.2f}".format(100 - ((y/validator) *)))))
                    values_near_to_goal.append(y)
                    values_tested.append(validator)
                else:
                    pass
                    

        except Exception as e:
            print(" exception by: "+str(e))
        else:
            pass
        finally:
            # print(" Test cases finished.")
            print(" Year tested %s"%year_tested)
            # print(" Status final by the bias: %s"%b)
            # print(" Total cases %s"%count_cases)
            
            # print(self.print_linear_equation(math_model['β0'], math_model['β1']))
            print(" Test cases aproved by the conditional %s"%len(values_near_to_goal))
            # print(values_near_to_goal)
            # print(" The total errores are %s percent "%(float(total_error / len(x_data_model))))

        # for a,b in zip(values_tested, values_near_to_goal):
        #     print(a,b)


    '''Function to support the conditional in above methods
        to be clare, is for only suppor.
    '''
            
    def print_linear_equation(self, beta_0, beta_1):

        return "Y = %s + (%s)X"%(beta_0, beta_1)

    def y_prediction(self, beta_0, beta_1, x_value):

        y = float("{0:.3f}".format(beta_0 + (x_value * beta_1)))
        return y

    def check_bias(self,bias, data, beta_0, beta_1, x_value):
        # the data is an array with values aproveds, only for testing whenever another 
        # bias is generated
        #-------------------------------------------------------------------------#
        #               Y = β0 + β1*x  (+)or(-)bias = value desired               #
        #-------------------------------------------------------------------------#

        counter = 0
        prediction = self.y_prediction(beta_0, beta_1, x_value)

        for x in data:
            if (prediction + bias) >= float(x) and (prediction + bias )<= float(x): 
                counter += 1
        return counter == len(data) 
    

    def cost_function(self,x_data, y_data, value_prediction):

        LIMITER_RANGE = len(x_data)
        mean_squared_error = 0.0
        # value prediction we will have to get using the math model
        # representing above; it's not neccessary to use the 
        # 
        for x in range(LIMITER_RANGE):

            mean_squared_error += (y_data[x] - value_prediction)**2

        return float(mean_squared_error/LIMITER_RANGE)


    





        










            
