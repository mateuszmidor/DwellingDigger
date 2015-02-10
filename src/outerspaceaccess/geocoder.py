# -*- coding: utf-8 -*-

'''
Created on 10 lut 2015

@author: m.midor
'''
from src.thirdparty.pygeocoder import pygeocoder

class Geocoder(object):
    '''
    This class allows you to turn address string like "Wielicka 32, Kraków, Polska" to longitude, lattitude tuple
    '''

    API_KEY = "AIzaSyAnelYhxyAsoYVLUouQ4pt7q9tlt4NunI0" # for 3demaniac account
    geocoder = pygeocoder.Geocoder(API_KEY)
    
    @staticmethod
    def geocode(address):
        return Geocoder.geocoder.geocode(address)[0].coordinates