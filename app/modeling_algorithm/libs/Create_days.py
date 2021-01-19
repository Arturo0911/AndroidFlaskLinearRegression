from app import app
from datetime import date, timedelta
import json

"""
    this file return all the days to be parsed
"""

class Create_days:

    def __init__(self):
        

        self.year_2017 = list()
        self.year_2018 = list()
        self.year_2019 = list()

        self.october_2016 = date(2016, 10, 1)
        self.january_2017 = date(2017, 1, 31)

        self.october_2017 = date(2017,10,1)
        self.january_2018 = date(2018,1,31)

        self.october_2018 = date(2018,10,1)
        self.january_2019 = date(2019,1,31)


        self.objects = {}

    def generate_appends(self):
        
        delta_2017 = self.january_2017 - self.october_2016
        delta_2018 = self.january_2018 - self.october_2017
        delta_2019 = self.january_2019 - self.october_2018


        for x in range(delta_2017.days + 1):
            days = self.october_2016 + timedelta(days=x)
            self.year_2017.append(str(days))

        self.objects[2017] = self.year_2017

        for x in range(delta_2018.days + 1):
            days = self.october_2017 + timedelta(days=x)
            self.year_2018.append(str(days))
        self.objects[2018] = self.year_2018


        for x in range(delta_2019.days +1):
            days = self.october_2018 + timedelta(days= x)
            self.year_2019.append(str(days))
        self.objects[2019] = self.year_2019


    def json_generate(self):
        
        with open('neuronal.json', 'w') as f:
            json.dump(self.objects,f,indent=4)

    def get_objects(self):
        
        return self.objects

    def return_days_keys(self):

        return self.objects.keys()








