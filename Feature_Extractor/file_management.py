#/////////////////////////////////////////////////////////////////
#Group of fuctions to remove and save queries response in an archive

import io
import re

def open_archive(file_name = ''):
    pass
    
def modify_archive(file_name = '', mode = 'a'):
    pass

def create_file(file_name = '', mode = 'w'):
    
    try:
        obj = open(file_name,'r')
    except:
        print(obj)
    else:
        pass