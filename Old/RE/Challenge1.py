#!/usr/local/bin/python3
# Jordan Matuszewski
# 13 March 2019

import re

def main():

    words = ['cōpare', 'cāper', 'mēber', 'mīe', 'ūbrella']
    for word in words:
        word = re.sub('[ā]',"am", word, flags = re.IGNORECASE)
        word = re.sub('[ō]',"om", word, flags = re.IGNORECASE)
        word = re.sub('[ē]',"em", word, flags = re.IGNORECASE)
        word = re.sub('[ī]',"im", word, flags = re.IGNORECASE)
        word = re.sub('[ū]',"um", word, flags = re.IGNORECASE)
        print(word)

if __name__ == '__main__':
    main()
