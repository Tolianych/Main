'''
Created on Jan 14, 2015

@author: s.botyan
'''

CASES = ['tc1', 'tc2', 'tc3', 'tc4', 'tc5']
result = ''
if __name__ == "__main__":
    for case in CASES:
        try:
            execfile('./tests/' + case + '.py')
            case_result = case + ': Passed\n'
        except Exception:
            case_result = case + ': Failed\n'
        result += case_result
    
    print result