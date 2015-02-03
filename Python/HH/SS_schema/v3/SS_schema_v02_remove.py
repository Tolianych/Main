# -*- coding: utf-8 -*-
'''
Created on Apr 29, 2014

@author: s.botyan

First You should do the next:
sudo apt-get install libpq-dev python-dev
sudo pip install psycopg2
'''

import psycopg2

CONNECT = "host='bear.pyn.ru' dbname='hhservice' user='dbadm' password='123'"

LIST_DELETION = ['company_info:2', 'company_info:3', 'company_info:4', 'company_info:5', 'company_info:6', 'company_info:7', 'company_info:8', 'salstat_lic_agr:2', 'salstat_lic_agr:3', 'salstat_lic_agr:4', 'salstat_lic_agr:5', 'salstat_lic_agr:6', 'salstat_lic_agr:7', 'salstat_lic_agr:8']



def update_sequence(cursor):
    cursor.execute("SELECT max(%s) FROM salarystat.%s;" % ('company_info_id', 'company_info'))
    max_id = cursor.fetchone()
    alter_seq = "ALTER SEQUENCE salarystat.%s RESTART WITH %s;" % ('company_info_company_info_id_seq', max_id[0])
    print alter_seq
    cursor.execute(alter_seq)
    
    cursor.execute("SELECT max(%s) FROM salarystat.%s;" % ('salstat_lic_agr_id', 'salstat_lic_agr'))
    max_id = cursor.fetchone()
    alter_seq = "ALTER SEQUENCE salarystat.%s RESTART WITH %s;" % ('salstat_lic_agr_salstat_lic_agr_id_seq', max_id[0])
    print alter_seq
    cursor.execute(alter_seq)    

def main():

    # print the connection string we will use to connect
    print "Connecting to database\n    ->%s" % (CONNECT)
 
    # get a connection, if a connect cannot be made an exception will be raised here
    conn = psycopg2.connect(CONNECT)
 
    # conn.cursor will return a cursor object, you can use this cursor to perform queries
    cursor = conn.cursor()
    print "Connected!\n"
    
    for value in LIST_DELETION:
        pair = value.split(':')
        delete = "DELETE FROM salarystat.%s WHERE %s_id = %s;" % (pair[0], pair[0], pair[1])
        print delete
        cursor.execute(delete)
    update_sequence(cursor)    
    conn.commit()
    print "Operation done successfully"
    conn.close()
     
if __name__ == "__main__":
    main()