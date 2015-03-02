'''
Created on 04-02-2015

@author: mateusz
'''
import unittest
from src.mvc.model.addressextractor.rankbased.dictionary import Dictionary
from src.mvc.model.addressextractor.rankbased.dictionary_entry import DictionaryEntry

class FileReaderStub:
    """ Stubs FileReader by returning predefined lines on read_lines(filename) call """
    
    def __init__(self, lines):
        self.lines = lines
        
    def read_lines(self, filename):
        return self.lines 


class DictionaryTest(unittest.TestCase):

    def __dictionary_has_entry(self, dictionary, name, original_form, address_type):
        for e in dictionary:
            if e.name == name and e.original_form == original_form and e.address_type == address_type:
                return True
            
        return False
    
    
    def test_append(self):
        """ Test if dictionary properly formats provided string and discards if empty """
        
        STREET = Dictionary.STREET
        d = Dictionary()
        d.append(DictionaryEntry("Addr1", "Addr1", STREET))  # should lowercase this string
        d.append(DictionaryEntry(" addr 2  ", " addr 2  ", STREET))  # should strip spaces
        d.append(DictionaryEntry("\n\raddr 3\t", "\n\raddr 3\t", STREET))  # should strip newline, carriage return and tabulator
        d.append(DictionaryEntry("addr4", "", STREET))  # should discard empty string
        d.append(DictionaryEntry("", "addr5", STREET))  # should discard empty string
        d.append(DictionaryEntry("addr6", "addr6", 11))  # should discard invalid address_type
        
        self.assertTrue(self.__dictionary_has_entry(d, "addr1", "Addr1", STREET), 
                        "'addr1, Addr1, STREET' not found in dictionary")
        
        self.assertTrue(self.__dictionary_has_entry(d, "addr 2", "addr 2", STREET), 
                        "'addr 2, addr 2, STREET' not found in dictionary")
        
        self.assertTrue(self.__dictionary_has_entry(d, "addr 3", "addr 3", STREET), 
                        "'addr 3, addr 3, STREET' not found in dictionary")
        
        self.assertEquals(len(d), 3, "Invalid entries have gotten into dictionary")
        
        
    def test_extend(self):
        """ Test if dictionary properly formats provided list of strings and discards empty strings """
        
        STREET = Dictionary.STREET
        entries = [DictionaryEntry("Addr1", "Addr1", STREET),
                   DictionaryEntry(" addr 2  ", " addr 2  ", STREET),
                   DictionaryEntry("\n\raddr 3\t", "\n\raddr 3\t", STREET),
                   DictionaryEntry("addr4", "", STREET),
                   DictionaryEntry("", "addr5", STREET),
                   DictionaryEntry("addr6", "addr6", 11)]
        
        d = Dictionary()
        d.extend(entries)
        
        self.assertTrue(self.__dictionary_has_entry(d, "addr1", "Addr1", STREET), 
                        "'addr1, Addr1, STREET' not found in dictionary")
        
        self.assertTrue(self.__dictionary_has_entry(d, "addr 2", "addr 2", STREET), 
                        "'addr 2, addr 2, STREET' not found in dictionary")
        
        self.assertTrue(self.__dictionary_has_entry(d, "addr 3", "addr 3", STREET), 
                        "'addr 3, addr 3, STREET' not found in dictionary")
        
        self.assertEquals(len(d), 3, "Invalid entries have gotten into dictionary")
        
    def test_sort_(self):       
        """ Test if dictionary can sort items longest to shortest """
        
        STREET = Dictionary.STREET
        entries = [DictionaryEntry("norm.", "norm.", STREET),
                   DictionaryEntry("longest", "longest", STREET),
                   DictionaryEntry("longer", "longer", STREET)]
        d = Dictionary(entries)
        d.sort_longest_first()
        
        i = iter(d)
        self.assertEqual(next(i).name, "longest", "'longest' entry should be at position 0")
        self.assertEqual(next(i).name, "longer", "'longer' entry should be at position 1")
        self.assertEqual(next(i).name, "norm.", "'norm.' entry should be at position 2")
        
        
    def test_from_file(self):
        """ Test if dictionary properly formats strings read from file and discards empty strings """
        
        STREET = Dictionary.STREET
        file_reader = FileReaderStub(["Addr1", " addr 2 ", "\n\raddr 3\t", ""])
        d = Dictionary.from_file("foo_bar.txt", STREET, file_reader)

        self.assertTrue(self.__dictionary_has_entry(d, "addr1", "Addr1", STREET), 
                        "'addr1, Addr1, STREET' not found in dictionary")
        
        self.assertTrue(self.__dictionary_has_entry(d, "addr 2", "addr 2", STREET), 
                        "'addr 2, addr 2, STREET' not found in dictionary")
        
        self.assertTrue(self.__dictionary_has_entry(d, "addr 3", "addr 3", STREET), 
                        "'addr 3, addr 3, STREET' not found in dictionary")
        
        self.assertEquals(len(d), 3, "Invalid entries have gotten into dictionary")
        
        
    def test_iterator_interface(self):
        """ Test if dictionary provides iterator that goes over all contained elements """
        
        STREET = Dictionary.STREET
        entries = [DictionaryEntry("addr1", "addr1", STREET),
                   DictionaryEntry("addr2", "addr2", STREET),
                   DictionaryEntry("addr3", "addr3", STREET)]
        d = Dictionary(entries)
        
        for e in d:
            self.assertTrue(e in entries, "Alien element found in dictionary: '%s, %s, %d'" % (e.name, e.original_form, e.address_type))
            entries.remove(e)
        self.assertEquals(len(entries), 0, "Dictionary iterator hasn't gone over all the elements")
           
           
    def test_len_interface(self):
        """ Test if len(dictionary) returns it's actual size """
        
        STREET = Dictionary.STREET
        d = Dictionary([])
        self.assertEqual(len(d), 0, "len(empty_dictionary) should return 0")
        
        entries = [DictionaryEntry("addr1", "addr1", STREET),
                   DictionaryEntry("addr2", "addr2", STREET),
                   DictionaryEntry("addr3", "addr3", STREET)]
        d = Dictionary(entries)
        self.assertEqual(len(d), 3, "len(3_elements_dictionary) should return 3")
        
        
        
if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
