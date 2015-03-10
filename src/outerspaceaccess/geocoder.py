# -*- coding: utf-8 -*-

'''
Created on 10 lut 2015

@author: m.midor
'''
from src.thirdparty.pygeocoder import pygeocoder
from src.thirdparty.pygeocoder.pygeolib import GeocoderError
import time

class Geocoder(object):
    '''
    This class allows you to turn address string like "Wielicka 32, Kraków, Polska" to longitude, lattitude tuple
    '''

    API_KEY = "AIzaSyAnelYhxyAsoYVLUouQ4pt7q9tlt4NunI0" # for 3demaniac account
    geocoder = pygeocoder.Geocoder(API_KEY)
    
    
    @staticmethod
    def geocode(address):
        """ Turn address into [longiture, latitude]. Max 5 geocodings/second due to google api limitation """
        
        MAX_ATTEMPTS = 10
        DELAY = 0.2
        
        for i in xrange(MAX_ATTEMPTS):
            result = Geocoder.__try_geocode(address)
            if result:
                return result
            
            print("geocode attempt %d failed. Trying again in %f seconds" % (i + 1, DELAY))
            time.sleep(DELAY) 
                
        raise RuntimeError("Giving up geocoding after %d attempts" % MAX_ATTEMPTS)
    
    
    @staticmethod
    def __try_geocode(address):
        try:
            coords = Geocoder.geocoder.geocode(address)[0].coordinates
            print("Successfully geocoded %s" % address)
            return coords
        except GeocoderError:
            print("Geocoder Exception - GeocoderError")
            return None 
        except IOError:
            print("Geocoder Exception - IOError")
            return None      
        except Exception:
            print("Geocoder Exception")
            return None      