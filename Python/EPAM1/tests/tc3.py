'''
Created on Jan 14, 2015

@author: s.botyan
'''
import logging
import os
from EPAM1.env import *
from EPAM1.actions import chmod, change_owner_group, modify_file

def prerequisits():
    logging.debug('Creating file')
    open(os.path.join(NAS, FILE), 'w')
    logging.debug('Applying chmode')
    chmod(774, NAS, FILE, SUDO_PASS)
    logging.debug('Changing file owner')
    change_owner_group(USER2, NAS, FILE, SUDO_PASS)
    logging.debug('--Prerequisits created--')
    
def cleanup():
    os.remove(os.path.join(NAS, FILE))
    
def main():
    logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s', filename='output_log.log',level=logging.DEBUG)
    
    logging.debug('---TESTCASE 3---')
    #Prerequisits
    prerequisits()
    #Step 1
    logging.debug('Trying to modify file')
    try:
        modify_file(NAS, FILE)
        logging.error('Its possible to modify File')
        logging.error('TESTCASE3 FAILED!')
        raise Exception('Test case failed')
    except Exception:
        logging.debug('Impossible to open File')
        
    #Step 2
    logging.debug('Applying chmod 776')
    chmod(776, NAS, FILE, SUDO_PASS)
    
    #Step 3
    logging.debug('Trying to open file')
    try:
        modify_file(NAS, FILE)
        logging.debug('File is modified')
    except Exception:
        logging.error('Impossible to modify File')
        logging.error('TESTCASE3 FAILED!')
        raise Exception('Test case failed')
        
    cleanup()
    
    logging.debug('TESTCASE3 completed successfully!')        
        
if __name__ == "__main__":
    main()