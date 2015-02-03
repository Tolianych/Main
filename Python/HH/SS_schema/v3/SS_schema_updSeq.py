# -*- coding: utf-8 -*-
'''
Created on Apr 07, 2014

@author: s.botyan

First You should do the next:
sudo apt-get install libpq-dev python-dev
sudo pip install psycopg2
'''

import psycopg2

CONNECT = "host='bear.pyn.ru' dbname='hhservice' user='dbadm' password='123'"

SEQUENCE_LIST = {'company_department' : 'company_department_company_department_id_seq',
                 'company_info' : 'company_info_company_info_id_seq',
                 'department_emp_group' : 'department_emp_group_department_emp_group_id_seq',
                 'employee' : 'employee_employee_id_seq',
                 'salstat_lic_agr' : 'salstat_lic_agr_salstat_lic_agr_id_seq'}


def update_sequence(cursor):
    for seq in SEQUENCE_LIST:
        cursor.execute("SELECT max(%s) FROM salarystat.%s" % (seq + '_id', seq))
        max_id = cursor.fetchone()

        alter_seq = "ALTER SEQUENCE salarystat.%s RESTART WITH %s;" % (SEQUENCE_LIST[seq], max_id[0] + 1)
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
    
    cursor.execute("SELECT max(company_info_id) FROM salarystat.company_info")
    max_id = cursor.fetchone()
    curr_id = max_id[0]
    
        
    update_sequence(cursor)
    
    conn.commit()
    
    print "Operation done successfully"
    conn.close()
     
if __name__ == "__main__":
    main()