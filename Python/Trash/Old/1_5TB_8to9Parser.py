import os

PATH = 'D:\\Polygon\\upgrade8to9\\'

def execute():
    file = open(str(PATH) + 'log.txt', 'r')
    logfile = file.read()
    result = open(str(PATH) + 'result.csv', 'w')
    
    search_start = 0
    task_start_date = 1
    while task_start_date != -1 :        
        task_start = logfile.find("DST 2013", search_start)
        task_start_date = logfile[task_start - 16 : task_start - 1]
        
        swpd = logfile[task_start + 172 : task_start + 177]
        free = logfile[task_start + 178 : task_start + 184]
        buff = logfile[task_start + 185 : task_start + 191]
        cache = logfile[task_start + 192 : task_start + 198]
        
        search_start = task_start + 205
        #print(task_start_date)
        #print(swpd)
        #print(free)
        #print(buff)
        #print(cache)
        result.write(task_start_date + ',' + swpd.strip() + ',' + free.strip() + ',' + buff.strip() + ',' + cache.strip() + '\n')    

if __name__ == '__main__':
    execute()
