'''
Created on 21-02-2015

@author: mateusz
'''
import codecs

class TextFileWriter(object):

    @staticmethod
    def write(filename, content):
        codecs.open(filename, mode="wb", encoding="utf-8").write(content)


        