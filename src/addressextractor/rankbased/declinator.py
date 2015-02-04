'''
Created on 04-02-2015

@author: mateusz
'''

class Declinator(object):
    '''
    This class declinates words
    '''
    
    NORMAL_MODAL = {"ska" : "skiej", # krakowskiej
                    "cka" : "ckiej", # tynieckiej
                    "ny"  : "nach",  # czyżynach
                    "czne": "cznym"  # slonecznym 
                    }
    
    


    @staticmethod
    def declinate_dictionary(dictionary):
        
        declinations = list()
        for address in dictionary:
            d = Declinator.generate_declination(address)
            declinations.append(d)
            
        map(dictionary.append, declinations)
        
    @staticmethod
    def generate_declination(address):
        
        for normal, modal in Declinator.NORMAL_MODAL.iteritems():
            if address.endswith(normal):
                return address.replace(normal, modal)
        
        # If no declination of address is possible, return empty string;
        # According the Dictionary policy, empty string will not be added
        return ""
        