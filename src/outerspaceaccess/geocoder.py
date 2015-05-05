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

    API_KEY = "AIzaSyAnelYhxyAsoYVLUouQ4pt7q9tlt4NunI0" # for 3demaniac account
    geocoder = pygeocoder.Geocoder(API_KEY)
    logger = Inject
    
    
    @staticmethod
    def geocode(address):
        """ Turn address into [latitude, longitude]. Max 5 geocodings/second due to google api limitation """
        
        MAX_ATTEMPTS = 10
        DELAY = 0.2
        
        for i in xrange(MAX_ATTEMPTS):
            latlong = Geocoder.__try_geocode(address)
            if latlong:
                return latlong
            
            Geocoder.logger.debug("Geocoding '%s' attempt %d failed. Trying again in %f seconds" % (address, i + 1, DELAY))
            time.sleep(DELAY) 
                
        raise RuntimeError("Giving up geocoding after %d attempts" % MAX_ATTEMPTS)
    
    
    @staticmethod
    def __try_geocode(address):
        try:
            latlong = Geocoder.geocoder.geocode(address)[0].coordinates
            return latlong
        except GeocoderError as e:
            Geocoder.logger.debug(str(e))
            return None 
        except IOError as e:
            Geocoder.logger.debug(str(e))
            return None      
        except Exception as e:
            Geocoder.logger.debug(str(e))
            return None      