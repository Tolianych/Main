'''
Created on 02-02-2014

@author: Tolianych
'''

import os

PATH = 'D:\\Polygon\\'

def fileScanner():
    #test = os.walk(PATH)
    #print test
    files = [os.path.join(dirpath, name)
                for dirpath, dirname, file_name in os.walk(PATH)
                for name in file_name]
    print files
    for filePath in files:
        if filePath[-3 : ] == 'mp3':            
            file_path_name, fileExt = os.path.splitext(filePath)
            rfind = file_path_name.rfind('\\')
            file_path = file_path_name[0 : rfind] + '\\'
            file_name = file_path_name[rfind + 1 : ] + '.mp3'
            file_extension = fileExt[1 : 4]            
            size = os.path.getsize(filePath)
            print file_path
            print file_name
            print file_extension
            print str(size)
            #string_name = file_path + ',' + file_name + ',' + file_extension + ',' + str(size)
            #print string_name

def execute():
    fileScanner()

if __name__ == '__main__':
    execute()