#!/usr/local/bin/python3
# Jordan Matuszewski
# 09 Janruary 2019
# Example
# Paul Evans
# 30 January 2019

import re
import Levenshtein
def main():
    with open('WLBeforeHamming.txt', 'r') as f_in:
        file = f_in.read()
        words_one = re.split('\W', file)
        words_two = words_one
        for word_one in words_one:
            for word_two in words_two:
                if len(word_one) == len(word_two):
                    if Levenshtein.hamming(word_one, word_two) == 1:
                        print(word_one, word_two)

if __name__ == '__main__':
    main()

