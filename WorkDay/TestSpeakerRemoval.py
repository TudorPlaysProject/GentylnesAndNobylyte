#!/usr/local/bin/python3
# Jordan Matuszewski
# 12 February 2019

import re

def main():

        with open('input.txt', 'r') as Input:


            lines = Input.readlines()

            for line in lines:
               # result = re.match(r'^the\b\s+\w+$', line, flags = re.IGNORECASE)
               # result = re.match(r'^[\w\.]+$', line, flags = re.IGNORECASE)
                 result = re.match("wt", line, flags = re.IGNORECASE) 
              #  result = re.match('wyth', line, flags = re.IGNORECASE)
                 if (result):
                    print(line)

if __name__ == '__main__':
    main()
