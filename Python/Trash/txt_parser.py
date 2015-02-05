'''
Created on Jan 26, 2015

@author: s.botyan
'''
strings = {}
string_number = 0
content = open('/home/botyan/pgadmin.log')
for line in content:
    itog = []
    date_time = line[:19]
    itog += date_time.split()

    info = line[20:].split(':')

    itog.append(info[0].rstrip())
    itog.append(info[1].lstrip())
    itog.append(info[2][:-1])
    string_number += 1
    strings[string_number] = itog

print strings
