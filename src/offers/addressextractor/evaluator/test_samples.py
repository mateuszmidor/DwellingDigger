'''
Created on 6 lut 2015

@author: m.midor
'''
from src.outerspaceaccess.text_file_reader import TextFileReader
from src.offers.addressextractor.evaluator.test_sample import TestSample

class TestSamples(list):
    '''
    This class is basically a collection of test samples. 
    It allows to read test samples from file
    '''

    @staticmethod
    def from_file(filename, file_reader = TextFileReader):
        samples = TestSamples()
        current = TestSample()
        
        # SOURCE FILE STRUCTURE:
        # source=string1
        # source=string2
        # (more sources)
        # expected=string3
        # # comment        
        
        for line in file_reader.read_lines(filename):
            key, value = TestSamples.__get_key_value(line)
             
            if key == "source":
                current.sources.append(value)
            elif key == "expected":
                current.expected_result = value
                samples.append(current)
                current = TestSample()
            elif key == "#":
                # ignore comment 
                pass
                
        return samples
        
    @staticmethod
    def __get_key_value(line):
        
        # comment case
        if line.startswith("#"):
            return ["#", line[1:]]
                
        # regular key=value case
        if "=" in line:
            key, value = line.split("=") 
            return [key, value.strip(u"\n\r\t ")]
        
        # invalid line
        return ["", ""]
        