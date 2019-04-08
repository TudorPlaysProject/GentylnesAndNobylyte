#!/usr/local/bin/python3
# Jordan Matuszewski
# 12 February 2019

import re

def main():

    with open('output.txt', 'w') as Output:
        with open('input.txt', 'r') as Input:


            lines = Input.readlines()

            for line in lines:
                result = re.match('^[A-Z]{1}$', line) 
                print(result) 
