'''
Created on Jan 28, 2015

@author: s.botyan
'''

input_list = [1, 2, 4, 5, 6, 7, 9, 13, 22, 23, 24, 25, 26, 27]


def convert(input_list):
    output = ''
    i = 0
    first_setted = False
    dash = False
    while i < len(input_list) - 1:
        if not first_setted:
            add = str(input_list[i])
            first_setted = True

        if input_list[i+1] == input_list[i] + 1:
            if not dash:
                add += '-'
                dash = True
        else:
            if str(input_list[i]) != add:
                add += str(input_list[i]) + ', '
            else:
                add += ', '
            first_setted = False
            dash = False
            output += add

        i += 1

        if i == len(input_list) - 1:
            output += add + str(input_list[i])

    return output


def unconvert(input_string):
    unconverted_string = ''
    list_range = input_string.split(', ')
    for num in list_range:
        if num.find('-') != -1:
            digits = num.split('-')
            unconverted_string += str(digits[0]) + ', '
            i = int(digits[0])
            while i != int(digits[1]):
                unconverted_string += str(i + 1) + ', '
                i += 1
        else:
            unconverted_string += str(num) + ', '
    unconverted_string = unconverted_string[:-2]

    return unconverted_string

if __name__ == '__main__':
    converted_list = convert(input_list)
    print converted_list
    unconverted_string = unconvert(converted_list)
    print unconverted_string
