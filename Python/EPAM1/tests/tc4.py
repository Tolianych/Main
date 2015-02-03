'''
Created on Jan 14, 2015

@author: s.botyan
'''
import logging
import os
from EPAM1.env import *
from EPAM1.actions import chmod, change_owner_group, execute_file

def prerequisits():
    logging.debug('Creating file')
    f = open(os.path.join(NAS, FILE), 'w')
    f.write("print 'Hello world!'")    
    logging.debug('Applying chmode')
    chmod(770, NAS, FILE, SUDO_PASS)
    logging.debug('Changing file owner')
    change_owner_group(USER2, NAS, FILE, SUDO_PASS)
    logging.debug('--Prerequisits created--')

def cleanup():
    os.remove(os.path.join(NAS, FILE))
    
def main():
    logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s', filename='output_log.log',level=logging.DEBUG)
    
    logging.debug('---TESTCASE 4---')
    #Prerequisits
    prerequisits()
    #Step 1
    logging.debug('Trying to execute file')
    try:
        execute_file(NAS, FILE)
        logging.error('Its possible to execute File')
        logging.error('TESTCASE4 FAILED!')
        raise Exception('Test case failed')
    except Exception:
        logging.debug('Impossible to execute File')
        
    #Step 2
    logging.debug('Applying chmod 777')
    chmod(777, NAS, FILE, SUDO_PASS)
    
    #Step 3
    logging.debug('Trying to open file')
    try:
        execute_file(NAS, FILE)
        logging.debug('File is executed')
    except Exception:
        logging.error('Impossible to execute File')
        logging.error('TESTCASE4 FAILED!')
        raise Exception('Test case failed')
        
    cleanup()
    
    logging.debug('TESTCASE4 completed successfully!')        
        
if __name__ == "__main__":
    main()