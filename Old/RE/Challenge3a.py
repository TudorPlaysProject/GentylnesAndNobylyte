#!/usr/local/bin/python3
# Jordan Matuszewski
# 25  March 2019

import re

def main():

        # words = ['aiu','aui','hih', 'juj', 'aiue']
        line = "foo bar aiu baz aui foo ba hih baz juj ."
        line = re.sub('((?<=[aeiou])u(?=[aeiou]))',"v", line, flags = re.IGNORECASE)
        line = re.sub('((?<=[aeiou])i(?=[aeiou]))',"j", line, flags = re.IGNORECASE)
        print(line)

if __name__ == '__main__':
    main()
