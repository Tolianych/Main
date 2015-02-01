'''
Created on Jan 24, 2014

@author: s.botyan
'''
import random
import string

SYMBOLS_QTY = 255 #quantity of symbols in result string

letters = string.letters
i = 1
random_string = ''
while i <= SYMBOLS_QTY:
    random_letter = random.choice(letters)
    random_string += random_letter
    i += 1
    
print random_string
