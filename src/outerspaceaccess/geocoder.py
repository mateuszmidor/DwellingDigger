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
        """ 
        Turn address into (latitude, longitude) tuple. 
        Max 5 geocodings/second possible due to google api limitation. 
        If geocoding failed - throws RuntimeError.
        """
        
        # as the geocoding depends on external service - allow a number of attempts before throwing error
        max_attempt_count = 10
        
        # this is the google api limitation of 5 geocodings/second
        delay_between_attempts = 0.2
        
        # do a series of geocoding attempts
        for n_attempt in xrange(max_attempt_count):
            latlong = Geocoder.__try_geocode_or_return_none(address)
            
            # if geocoding successful - return the coordinates
            if latlong:
                return latlong
            
            # geocoding not successful
            Geocoder.logger.debug("Geocoding '%s' attempt %d failed. Trying again in %f seconds" % 
                                  (address, n_attempt + 1, delay_between_attempts))
            time.sleep(delay_between_attempts) 
             
        # all attempts failed   
        raise RuntimeError("Giving up geocoding after %d attempts" % max_attempt_count)
    
    
    @staticmethod
    def __try_geocode_or_return_none(address):
        """ 
        Try to geocode the address.
        If successful - return (latitude, longitude) tuple.
        If failure - log failure reason and return None.
        """
        
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
        