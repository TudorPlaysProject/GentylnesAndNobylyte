#!/usr/local/bin/python3
# Jordan Matuszewski
# 12 February 2019

import re

def main():

    with open('X_Gentylnes_and_Nobylyte_AfterER.txt', 'w') as Output:
        with open('X_Gentylnes_and_Nobylyte.txt', 'r') as Input:


            lines = Input.readlines()

            for line in lines:

                line = re.sub('&','[and]', line, flags = re.IGNORECASE)
                line = re.sub('{per}','per', line, flags = re.IGNORECASE)
                line = re.sub('{is}','is', line, flags = re.IGNORECASE)
                line = re.sub('page [unnumbered]',"", line, flags = re.IGNORECASE)
                line = re.sub('❡',"", line, flags = re.IGNORECASE)

                Output.write(line)


if __name__ == '__main__':
    main()

