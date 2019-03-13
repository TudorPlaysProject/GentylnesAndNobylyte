#!/usr/local/bin/python3
# Jordan Matuszewski
# 13 March 2019

import re

def main():

    words = ['{nut}ella', '{}', 'mam{}', '{yellow}', 'yum{my}']
    for word in words:
        word = re.sub('\{',"", word, flags = re.IGNORECASE)
        word = re.sub('\}',"", word, flags = re.IGNORECASE)
        print(word)

if __name__ == '__main__':
    main()
