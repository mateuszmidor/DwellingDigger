# -*- coding: utf-8 -*-

'''
Created on 10 lut 2015

@author: m.midor
'''
from src.thirdparty.pygeocoder import pygeocoder
from src.thirdparty.pygeocoder.pygeolib import GeocoderError
import time
from src.ioc.dependency_injector import DependencyInjector, Inject

@DependencyInjector("logger")
class Geocoder(object):
    '''
    This class allows you to turn address string like "Wielicka 32, Kraków, Polska" to longitude, lattitude tuple
    '''

    # google API KEY for 3demaniac account
    API_KEY = "AIzaSyAnelYhxyAsoYVLUouQ4pt7q9tlt4NunI0" 
    geocoder = pygeocoder.Geocoder(API_KEY)
    logger = Inject
    
    
    @staticmethod
    def geocode(address):
        """ Turn address into [latitude, longitude]. Max 5 geocodings/second due to google api limitation """
        
        max_attempt_count = 10
        delay_between_attempts = 0.2
        
        for i in xrange(max_attempt_count):
            latlong = Geocoder.__try_geocode(address)
            if latlong:
                return latlong
            
            Geocoder.logger.debug("Geocoding '%s' attempt %d failed. Trying again in %f seconds" % 
                                  (address, i + 1, delay_between_attempts))
            time.sleep(delay_between_attempts) 
                
        raise RuntimeError("Giving up geocoding after %d attempts" % max_attempt_count)
    
    
    @staticmethod
    def __try_geocode(address):
        try:
            latlong = Geocoder.geocoder.geocode(address)[0].coordinates
            return latlong
        except GeocoderError as error:
            Geocoder.logger.debug(str(error))
            return None 
        except IOError as error:
            Geocoder.logger.debug(str(error))
            return None      
        except Exception as error:
            Geocoder.logger.debug(str(error))
            return None      
        