'''
Created on Jan 20, 2015

@author: s.botyan
'''
text_file = open("something.txt")
text = text_file.read()
list_strings = text.splitlines()

count_dict = {}

for string in list_strings:
    list_words = string.split(" ")

    for word in list_words:
        # filtering all symbols except alphabet
        letters_count = len(filter(lambda x: x.isalpha(), word))

        if letters_count == 0:
            break

        # number of occurrences of letters_count into the dictionary
        qty = count_dict.get(letters_count, 0) + 1

        pair_length_count = {letters_count: qty}
        count_dict.update(pair_length_count)

for pair in count_dict:
    print "%s - %s" % (pair, count_dict[pair])
