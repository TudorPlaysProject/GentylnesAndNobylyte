#!/usr/local/bin/python3
# Jordan Matuszewski
# 01 February 2019

import re
import Levenshtein
def main():
    with open('WLAfterLD.txt', 'w') as the_file:
        with open('WLBeforeLD.txt', 'r') as f_in:
            file = f_in.read()
            words_one = re.split('\W', file)
            words_two = words_one
            for word_one in words_one:
                for word_two in words_two:
                    if len(word_one) == len(word_two):
                        if Levenshtein.distance(word_one, word_two) == 1:
                            the_file.write(word_one +" "+ word_two + '\n')

if __name__ == '__main__':
    main()

