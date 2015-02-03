'''
Created on Jan 14, 2015

@author: s.botyan
'''
import logging
import os
from EPAM1.env import *
from EPAM1.actions import chmod, change_owner_group, open_file

def prerequisits():
    logging.debug('Creating file')
    open(os.path.join(NAS, FILE), 'w')
    logging.debug('Applying chmode')
    chmod(770, NAS, FILE, SUDO_PASS)
    logging.debug('Changing file owner')
    change_owner_group(USER2, NAS, FILE, SUDO_PASS)
    logging.debug('--Prerequisits created--')
    
def cleanup():
    os.remove(os.path.join(NAS, FILE))
    
def main():
    logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s', filename='output_log.log',level=logging.DEBUG)
    
    logging.debug('---TESTCASE 2---')
    #Prerequisits
    prerequisits()
    #Step 1
    logging.debug('Trying to open file')
    try:
        open_file(NAS, FILE)
        logging.error('It\'s possible to open file by unautorized user')
        raise Exception('Test case failed')
    except Exception:
        logging.debug('Impossible to open File')
        pass
    
    #Step 2
    logging.debug('Applying chmod 777')
    chmod(777, NAS, FILE, SUDO_PASS)
    
    #Step 3
    logging.debug('Trying to open file')
    try:
        open_file(NAS, FILE)
        logging.debug('File is opened')
    except Exception:
        logging.error('Impossible to open File')
        logging.error('TESTCASE2 FAILED!')
        raise Exception('Test case failed')
        
    cleanup()
    
    logging.debug('TESTCASE2 completed successfully!')        
        
if __name__ == "__main__":
    main()