# -*- coding: utf-8 -*-
'''
Created on Apr 08, 2014

@author: s.botyan

First You should do the next:
sudo apt-get install libpq-dev python-dev
sudo pip install psycopg2
'''

import psycopg2

CONNECT = "host='bear.pyn.ru' dbname='hhservice' user='dbadm' password='123'"

DELETE_SCRIPT = """

"""

def run_script(cursor, curr_id, table):
    table_id = curr_id
    for line in table.split('\n'):
        #print line.format(table_id)
        query = line.format(table_id)
        print query
        cursor.execute(query)
        table_id += 1    

def main():

    # print the connection string we will use to connect
    print "Connecting to database\n    ->%s" % (CONNECT)
 
    # get a connection, if a connect cannot be made an exception will be raised here
    conn = psycopg2.connect(CONNECT)
 
    # conn.cursor will return a cursor object, you can use this cursor to perform queries
    cursor = conn.cursor()
    print "Connected!\n"
    
    for line in DELETE_SCRIPT.split('\n'):
        print line
        cursor.execute(line)
        
    conn.commit()
    print "Operation done successfully"
    conn.close()
     
if __name__ == "__main__":
    main()