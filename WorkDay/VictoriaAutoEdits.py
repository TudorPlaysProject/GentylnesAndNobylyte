#!/usr/local/bin/python3
# Jordan Matuszewski
# 12 February 2019

import re

def main():

    with open('output.txt', 'w') as Output:
        with open('input.txt', 'r') as Input:


            lines = Input.readlines()

            for line in lines:

                line = re.sub('&',"and", line, flags = re.IGNORECASE)
                line = re.sub('〈◊+〉',"", line, flags = re.IGNORECASE)
                line = re.sub('\b[^aeiou\s]{1}\b',"", line, flags = re.IGNORECASE)
                line = re.sub('(page\s+\[unnumbered\])',"", line, flags = re.IGNORECASE)
                line = re.sub('¶',"", line)
                line = re.sub('eue',"eve", line, flags = re.IGNORECASE) #haue to have
                line = re.sub('lyst',"lest", line, flags = re.IGNORECASE) #noblyst to noblest
                line = re.sub('aue',"ave", line, flags = re.IGNORECASE) #euer to ever
                line = re.sub('hyn(?=[^aeiou])',"hin", line, flags = re.IGNORECASE) #thyng to thing
                line = re.sub('\b(y)(?=[^ts])[a-z]{1}\b', "wi", line, flags = re.IGNORECASE) #wyse to wise
                line = re.sub('\bry(?=[^aeiou])+', "ri", line, flags = re.IGNORECASE) #ryches to riches
                line = re.sub('eri\b',"ery", line, flags = re.IGNORECASE) #eri to ery (doesn't work, suspect it has something to do with eue being changed)
                line = re.sub('\bbi\b',"by", line, flags = re.IGNORECASE) #doesnt work with word boundary, but changes false positives without
                line = re.sub('∣',"", line)
                line = re.sub('\b[^aeiou\s]{1}\b',"", line)
                # line = re.sub('[p̄]',"pir", line, flags = re.IGNORECASE)
                line = re.sub('[ā]',"am", line, flags = re.IGNORECASE)
                line = re.sub('((?<! c)ō)',"om", line, flags = re.IGNORECASE)
                line = re.sub('((?<=c)ō)',"on", line, flags = re.IGNORECASE)
                line = re.sub('[ē]',"em", line, flags = re.IGNORECASE)
                line = re.sub('[ī]',"im", line, flags = re.IGNORECASE)
                line = re.sub('[ū]',"um", line, flags = re.IGNORECASE)
                line = re.sub(r'{(\w+)}', '\\1', line)
                line = re.sub('((?<=[aeiou])u(?=[aeiou]))',"v", line, flags = re.IGNORECASE)
                line = re.sub('((?<=[aeiou])i(?=[aeiou]))',"j", line, flags = re.IGNORECASE)
                Output.write(line)


if __name__ == '__main__':
    main()

