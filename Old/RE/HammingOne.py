#!/usr/local/bin/python3
# Jordan Matuszewski
# 12 Janruary 2019

import re
import Levenshtein
def main():
    with open('WLAfterHamming.txt', 'w') as the_file:
        with open('WLBeforeHamming.txt', 'r') as f_in:
            file = f_in.read()
            words_one = re.split('\W', file)
            words_two = words_one
            for word_one in words_one:
                for word_two in words_two:
                    if len(word_one) == len(word_two):
                        if Levenshtein.hamming(word_one, word_two) == 1:
                            the_file.write(word_one +" "+ word_two + '\n')

if __name__ == '__main__':
    main()

