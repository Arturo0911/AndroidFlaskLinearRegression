import requests
from urllib.request import urlopen
from urllib.error import HTTPError


class API_values:

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
        
        self.weatherbi_key = 'c09b8f1a39d14a8bb9d343ccab529441'
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


    def get_average_to_clouds(self):
        pass

    
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

    
    





