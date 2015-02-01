import os

PATH = 'D:\\Polygon\\Performance\\'

def execute():
    file = open(str(PATH) + 'log.xml', 'r')
    logfile = file.read()
    result = open(str(PATH) + 'result.csv', 'w')
    
    search_start = 0
    task_start_date = 1
    while (task_start_date != -1):        
        task_start = logfile.find("from 'idle' to 'running'", search_start)
        task_start_date = logfile[task_start + 44 : task_start + 52]
        task_start_time = logfile[task_start + 53 : task_start + 61]
        
        task_end = logfile.find("from 'running' to 'idle'", task_start + 70)
        task_end_date = logfile[task_end + 44 : task_end + 52]
        task_end_time = logfile[task_end + 53 : task_end + 61]
        
        #IN CASE OF MANY TASKS
        #task_start = logfile.find("16'' changed its state from 'idle' to 'running'", search_start)
        #task_start_date = logfile[task_start + 67 : task_start + 75]
        #task_start_time = logfile[task_start + 76 : task_start + 84]
        
        #task_end = logfile.find("16'' changed its state from 'running' to 'idle'", task_start + 93)
        #task_end_date = logfile[task_end + 67 : task_end + 75]
        #task_end_time = logfile[task_end + 76 : task_end + 84]
        
        search_start = task_end + 93
        result.write(task_start_date + ',' + task_start_time + ',' + task_end_date + ',' + task_end_time + '\n')    

if __name__ == '__main__':
    execute()