'''
Created on Jan 29, 2015

@author: s.botyan
'''

CHART_STRING = [5, 2, 1, 0, 3, 6, 8, 4]

lines_qty_list = CHART_STRING[0 : ]
lines_qty_list.sort()
lines_qty = lines_qty_list[-1]

columns_qty = len(CHART_STRING)

lines_dict = {} 
line_number = 1

while line_number <= lines_qty:
    line = []
    for num in CHART_STRING:
        if num >= line_number:
            line += '*'
        else:
            line += ' '
    
    lines_dict[line_number] = line
    line_number += 1

i = lines_qty

while i >= 1:
    output_line = ''
    for symbol in lines_dict[i]:
        output_line += symbol
    print output_line
    i -= 1
