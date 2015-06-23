'''
Created on 12-02-2015

FACADE. All needed functionality from model package you can find here
@author: mateusz
'''

from src.mvc.model.addressextractor.address_extractor import AddressExtractor
from src.mvc.model.gumtree.gumtree import Gumtree
from src.mvc.model.gumtree.offer_extractor import OfferExtractor as GumtreeOfferExtractor
from src.mvc.model.olx.offer_extractor import OfferExtractor as OlxOfferExtractor
from src.mvc.model.olx.olx import Olx
from src.outerspaceaccess.web_document_fetcher import WebDocumentFetcher
from src.multitasking.teamwork import TeamWork
from src.ioc.dependency_injector import DependencyInjector, Inject
from src.outerspaceaccess.cachinggeocoder import CachingGeocoder
from src.mvc.model.offer_processing_exception import OfferProcessingException


@DependencyInjector("config")
class Offers(object):
    '''
    This class is a facade for retrieving offers.
    Use it when you want to get actual offers matching criteria described by OfferParams. 
    '''
    
    config = Inject
             
            
    @staticmethod
    def get_from_all_sources(offer_params, max_offer_count=5, max_parallel_count=5):
        """ Gets offers from Olx and Gumtree filtered with criteria described by OfferParams. """
        
        geocoder = Offers.__get_geocoder()
        address_extractor = Offers.__get_address_extractor(offer_params.get_city())
        team_work = TeamWork.start_work(Offers.__fetch_and_compose_offer, max_parallel_count)
        
        for url in Gumtree.get_urls(offer_params, max_offer_count / 2):
            team_work.add_work((url, GumtreeOfferExtractor, address_extractor, geocoder))
             
        for url in Olx.get_urls(offer_params, max_offer_count / 2):
            team_work.add_work((url, OlxOfferExtractor, address_extractor, geocoder))
        
        for offer in team_work.end_work():
            yield offer
            
            
    @staticmethod
    def __get_geocoder():
        """ Create a new caching geocoder """
        
        cachefile = Offers.config.get("PATHS", "geocodingsCache")
        return CachingGeocoder(cachefile)


    @staticmethod
    def __get_address_extractor(city):
        """ Create a new address extractor specialized for extracting addresses in given city """
        
        address_extractor = AddressExtractor.for_city(city)
        address_extractor.city = city
        address_extractor.country = "Polska"
        return address_extractor
        
       
    @staticmethod 
    def __fetch_and_compose_offer(work_data):
        """
        This method unpacks offer url, offer_extrator, address_extractor, geocoder,
        downloads offer page from url and extracts offer details, then
        extracts address from offer details, finds address geolocation,
        and returns offer details along with url, address and geolocation.
        """
        
        try:
            # unpack the work data
            url, offer_extrator, address_extractor, geocoder = work_data
            
            # fetch the offer web page
            offer_page = WebDocumentFetcher.fetch(url)
            
            # parse the page and extract offer details
            offer = offer_extrator.extract(offer_page)
            
            # find address in the offer
            street_or_district = address_extractor.extract([offer["address_section"], 
                                                            offer["title"], 
                                                            offer["summary"]]) 
             
            # form nice full address string containing street, city and country
            full_address = Offers.__format_full_address(street_or_district, 
                                                        address_extractor.city, 
                                                        address_extractor.country)
            
            # add the nice address to offer details
            offer["address"] = full_address
            
            # geocode the address and add it to offer details
            latlong = geocoder.geocode(full_address)
            offer["latlong"] = latlong
            
            # add the offer page url to offer details
            offer["url"] = url 
         
            return offer
        
        except Exception as e:
            raise OfferProcessingException(url, e)     
        

    @staticmethod
    def __format_full_address(street_district, city, country):
        """ Compose address string from street, city and country. street is optional """
        
        if street_district:
            return u"{0}, {1}, {2}".format(street_district, city, country)
        else:
            return u"{0}, {1}".format(city, country)
