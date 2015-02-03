'''
Created on Jan 14, 2015

@author: s.botyan
'''
import logging
import os

from EPAM1.env import *
from EPAM1.actions import find_owner, change_owner

def cleanup():
    os.remove(os.path.join(NAS, FILE))

def main():
    logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s', filename='output_log.log',level=logging.DEBUG)
    
    logging.debug('---TESTCASE 1---')
    #Step 1
    logging.debug('Creating file')
    open(os.path.join(NAS, FILE), 'w')
    
    #Step 2
    logging.debug('Checking file owner')
    owner = find_owner(NAS, FILE)
    if owner == USER1:
        logging.debug('File owner is User1')
    else:
        logging.error('File owner is not User1')
        raise Exception('Test case failed')
    
    #Step 3
    logging.debug('Changing file owner')
    change_owner(USER2, NAS, FILE, SUDO_PASS)
    
    #Step 4
    owner = find_owner(NAS, FILE)
    if owner == USER2:
        logging.debug('File owner is User2')
    else:
        logging.error('File owner is not User2')
        raise Exception('Test case failed')
    
    #Step 5
    logging.debug('Changing file owner back to User1')
    change_owner(USER1, NAS, FILE, SUDO_PASS)
    
    #Step 6
    owner = find_owner(NAS, FILE)
    if owner == USER1:
        logging.debug('File owner is User1')
    else:
        logging.error('File owner is not User1')
        raise Exception('Test case failed')   
    
    cleanup()
    
    logging.debug('TESTCASE1 completed successfully!')

if __name__ == "__main__":
    main()