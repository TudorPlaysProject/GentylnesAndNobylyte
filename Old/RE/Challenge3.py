#!/usr/local/bin/python3
# Jordan Matuszewski
# 25  March 2019

import re

def main():

    words = ['aiu','aui','hih', 'juj', 'aiue']
    for word in words:
        word = re.sub('((?<=[aeiou])u(?=[aeiou]))',"v", word, flags = re.IGNORECASE)
        word = re.sub('((?<=[aeiou])i(?=[aeiou]))',"j", word, flags = re.IGNORECASE)
        print(word)

if __name__ == '__main__':
    main()
