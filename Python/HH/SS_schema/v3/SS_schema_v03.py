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

INSERT_company_info = """INSERT INTO salarystat.company_info VALUES ({0}, 333, 'CONSORT Group', 1, 2001, NULL, 1, NULL, 1, 1, NULL, NULL, 1, NULL, NULL, NULL, 4, '2014-03-25 16:37:17.29', NULL);
INSERT INTO salarystat.company_info VALUES ({0}, 1068, 'Cornerstone', 1, 2002, NULL, 1, NULL, 1, 1, NULL, NULL, 1, NULL, NULL, NULL, 4, '2014-03-25 16:48:32.531', NULL);
INSERT INTO salarystat.company_info VALUES ({0}, 272, 'DHL Express', 1, 2003, NULL, 1, NULL, 1, 1, NULL, NULL, 1, NULL, NULL, NULL, 4, '2014-03-25 16:55:04.021', NULL);
INSERT INTO salarystat.company_info VALUES ({0}, 180, 'Агентство Контакт', 1, 2004, NULL, 1, NULL, 1, 1, NULL, NULL, 1, NULL, NULL, NULL, 4, '2014-03-25 16:59:01.993', NULL);
INSERT INTO salarystat.company_info VALUES ({0}, 35566, 'Оптима, Группа компаний', 1, 2006, NULL, 1, NULL, 1, 1, NULL, NULL, 1, NULL, NULL, NULL, 4, '2014-03-25 17:01:36.97', NULL);
INSERT INTO salarystat.company_info VALUES ({0}, 2343, 'Спортмастер', 1, 2007, NULL, 1, NULL, 1, 1, NULL, NULL, 1, NULL, NULL, NULL, 4, '2014-03-25 17:05:04.524', NULL);
INSERT INTO salarystat.company_info VALUES ({0}, 985, 'ЮНИТИ, Кадровый центр', 1, 2011, NULL, 1, NULL, 1, 1, NULL, NULL, 1, NULL, NULL, NULL, 4, '2014-03-25 17:08:10.813', NULL);"""

INSERT_company_department = """INSERT INTO salarystat.company_department VALUES ({0}, {0}, 1, 'Магазин', NULL, NULL, NULL, 519, NULL, NULL);
INSERT INTO salarystat.company_department VALUES ({0}, {0}, 1, NULL, NULL, NULL, NULL, 519, NULL, NULL);
INSERT INTO salarystat.company_department VALUES ({0}, {0}, 1, NULL, NULL, NULL, NULL, 519, NULL, NULL);
INSERT INTO salarystat.company_department VALUES ({0}, {0}, 1, NULL, NULL, NULL, NULL, 519, NULL, NULL);
INSERT INTO salarystat.company_department VALUES ({0}, {0}, 1, NULL, NULL, NULL, NULL, 519, NULL, NULL);
INSERT INTO salarystat.company_department VALUES ({0}, {0}, 1, NULL, NULL, NULL, NULL, 519, NULL, NULL);
INSERT INTO salarystat.company_department VALUES ({0}, {0}, 1, NULL, NULL, NULL, NULL, 519, NULL, NULL);"""

INSERT_company_info_industry = """INSERT INTO salarystat.company_info_industry VALUES ({0}, 15, 519);
INSERT INTO salarystat.company_info_industry VALUES ({0}, 15, 519);
INSERT INTO salarystat.company_info_industry VALUES ({0}, 15, 519);
INSERT INTO salarystat.company_info_industry VALUES ({0}, 15, 519);
INSERT INTO salarystat.company_info_industry VALUES ({0}, 15, 519);
INSERT INTO salarystat.company_info_industry VALUES ({0}, 15, 519);
INSERT INTO salarystat.company_info_industry VALUES ({0}, 15, 519);"""

INSERT_department_emp_group ="""INSERT INTO salarystat.department_emp_group VALUES ({0}, {1}, 1010000, 1010001, NULL);
INSERT INTO salarystat.department_emp_group VALUES ({0}, {1}, 1170000, 1170003, NULL);
INSERT INTO salarystat.department_emp_group VALUES ({0}, {1}, 1010000, 1010001, NULL);
INSERT INTO salarystat.department_emp_group VALUES ({0}, {1}, 1170000, 1170003, NULL);
INSERT INTO salarystat.department_emp_group VALUES ({0}, {1}, 1010000, 1010001, NULL);
INSERT INTO salarystat.department_emp_group VALUES ({0}, {1}, 1170000, 1170003, NULL);
INSERT INTO salarystat.department_emp_group VALUES ({0}, {1}, 1010000, 1010001, NULL);
INSERT INTO salarystat.department_emp_group VALUES ({0}, {1}, 1170000, 1170003, NULL);
INSERT INTO salarystat.department_emp_group VALUES ({0}, {1}, 1010000, 1010001, NULL);
INSERT INTO salarystat.department_emp_group VALUES ({0}, {1}, 1170000, 1170003, NULL);
INSERT INTO salarystat.department_emp_group VALUES ({0}, {1}, 1010000, 1010001, NULL);
INSERT INTO salarystat.department_emp_group VALUES ({0}, {1}, 1170000, 1170003, NULL);
INSERT INTO salarystat.department_emp_group VALUES ({0}, {1}, 1010000, 1010001, NULL);
INSERT INTO salarystat.department_emp_group VALUES ({0}, {1}, 1170000, 1170003, NULL);"""

INSERT_employee = """INSERT INTO salarystat.employee VALUES ({0}, {1}, 1, 'Главный', '', 1, 60000, 750000, 720000);
INSERT INTO salarystat.employee VALUES ({0}, {1}, 6, 'Тестер', '', 10, 30000, 380000, 360000);
INSERT INTO salarystat.employee VALUES ({0}, {1}, 1, 'Дирик', '', 1, 70000, 850000, 840000);
INSERT INTO salarystat.employee VALUES ({0}, {1}, 6, 'Тестировщик', '', 15, 40000, 500000, 480000);
INSERT INTO salarystat.employee VALUES ({0}, {1}, 1, 'Генеральный', '', 1, 80000, 1000000, 960000);
INSERT INTO salarystat.employee VALUES ({0}, {1}, 6, 'Тестировщик ручной', '', 7, 50000, 630000, 600000);
INSERT INTO salarystat.employee VALUES ({0}, {1}, 1, 'ГенДиректор', '', 1, 90000, 1100000, 1080000);
INSERT INTO salarystat.employee VALUES ({0}, {1}, 6, 'Тестеровщег', 'тестер', 4, 70000, 860000, 840000);
INSERT INTO salarystat.employee VALUES ({0}, {1}, 1, 'Дирик', 'маловато', 1, 35000, 450000, 420000);
INSERT INTO salarystat.employee VALUES ({0}, {1}, 6, 'Тесты делает', '', 8, 35000, 450000, 420000);
INSERT INTO salarystat.employee VALUES ({0}, {1}, 1, 'Ген.Дир.', '', 1, 75000, 950000, 900000);
INSERT INTO salarystat.employee VALUES ({0}, {1}, 6, 'Спец по Тестированию', '', 12, 55000, 680000, 660000);
INSERT INTO salarystat.employee VALUES ({0}, {1}, 1, 'ГенДиректор', '', 1, 82000, 1000000, 990000);
INSERT INTO salarystat.employee VALUES ({0}, {1}, 6, 'Тестировщик ПО', '', 4, 65000, 790000, 780000);"""

INSERT_salstat_lic_agr = """INSERT INTO salarystat.salstat_lic_agr VALUES ({0}, '2014-03-25 16:11:07.628', 440541, 333, 'CONSORT Group');
INSERT INTO salarystat.salstat_lic_agr VALUES ({0}, '2014-03-25 16:46:45.25', 37, 1068, 'Cornerstone');
INSERT INTO salarystat.salstat_lic_agr VALUES ({0}, '2014-03-25 16:52:48.448', 2137755, 272, 'DHL Express');
INSERT INTO salarystat.salstat_lic_agr VALUES ({0}, '2014-03-25 16:57:17.414', 1687754, 180, 'Агентство Контакт');
INSERT INTO salarystat.salstat_lic_agr VALUES ({0}, '2014-03-25 16:59:54.994', 2285218, 35566, 'Оптима, Группа компаний');
INSERT INTO salarystat.salstat_lic_agr VALUES ({0}, '2014-03-25 17:02:50.669', 663627, 2343, 'Спортмастер');
INSERT INTO salarystat.salstat_lic_agr VALUES ({0}, '2014-03-25 17:06:17.879', 5802297, 985, 'ЮНИТИ, Кадровый центр');"""

TABLES = [INSERT_company_info, INSERT_company_department, INSERT_company_info_industry, INSERT_salstat_lic_agr]

SEQUENCE_LIST = {'company_department' : 'company_department_company_department_id_seq',
                 'company_info' : 'company_info_company_info_id_seq',
                 'department_emp_group' : 'department_emp_group_department_emp_group_id_seq',
                 'employee' : 'employee_employee_id_seq',
                 'salstat_lic_agr' : 'salstat_lic_agr_salstat_lic_agr_id_seq'}

inserted_data = []

def run_script(cursor, curr_id, table):
    table_id = curr_id
    for line in table.split('\n'):
        #print line.format(table_id)
        query = line.format(table_id)
        print query
        cursor.execute(query)
        
        if table == INSERT_salstat_lic_agr:
            inserted_data.append('salstat_lic_agr:%s' % table_id)
        elif table == INSERT_company_info:
            inserted_data.append('company_info:%s' % table_id)
        
        table_id += 1    

def update_sequence(cursor, curr_id):
    for seq in SEQUENCE_LIST:
        cursor.execute("SELECT max(%s) FROM salarystat.%s" % (seq + '_id', seq))
        max_id = cursor.fetchone()

        alter_seq = "ALTER SEQUENCE salarystat.%s RESTART WITH %s;" % (SEQUENCE_LIST[seq], max_id[0])
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
    curr_id = max_id[0] + 1
    
    for table in TABLES:
        run_script(cursor, curr_id, table)  
        
    #INSERT INTO salarystat.department_emp_group
    table_id = curr_id
    company_department_id = curr_id
    inc_flag = 1 #flag to increment once per two 
    for line in INSERT_department_emp_group.split('\n'):
        print line.format(table_id, company_department_id)
        cursor.execute(line.format(table_id, company_department_id))
        if inc_flag % 2 == 0:
            company_department_id += 1
        inc_flag += 1
        table_id += 1
    
    #INSERT INTO salarystat.employee
    #ATTENTION TO REFERENCES salarystat.department_emp_group
    table_id = curr_id
    for line in INSERT_employee.split('\n'):
        print line.format(table_id, table_id)
        cursor.execute(line.format(table_id, table_id))
        table_id += 1    
    
    print "Updating sequences \n"    
    update_sequence(cursor, curr_id)
    
    conn.commit()
    
    print "Operation done successfully"
    print "List for deletion of inserted data:"
    print inserted_data
    conn.close()
     
if __name__ == "__main__":
    main()