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
                line = re.sub('^[A-Z]{1}$',"", line, flags = re.IGNORECASE)
                line = re.sub('^\.[A-Z]{1}\.$',"", line, flags = re.IGNORECASE)
                line = re.sub('(page\s+\[unnumbered\])',"", line, flags = re.IGNORECASE)
                line = re.sub('¶',"", line)
              # line = re.sub('lyst',"lest", line, flags = re.IGNORECASE) #noblyst to noblest
              # line = re.sub('hyn(?=[^aeiou])',"hin", line, flags = re.IGNORECASE) #thyng to thing
                line = re.sub('\b(y)(?=[^ts])[a-z]{1}\b', "wi", line, flags = re.IGNORECASE) #wyse to wise
                line = re.sub('\bry(?=[^aeiou])+', "ri", line, flags = re.IGNORECASE) #ryches to riches
                line = re.sub('eri\b',"ery", line, flags = re.IGNORECASE) #eri to ery (doesn't work, suspect it has something to do with eue being changed)
                line = re.sub(r'\bbi\b',"by", line) #doesnt work with word boundary, but changes false positives without
                line = re.sub(r'\bBi\b',"By", line) #doesnt work with word boundary, but changes false positives without
                line = re.sub('∣',"", line)
                line = re.sub('\b[^aeiou\s]{1}\b',"", line)
                line = re.sub(r'{(\w+)}', '\\1', line)
                line = re.sub(r'\bys\b', "is", line)
                #No genitive "ys" in G&N 
                line = re.sub(r'\byf\b',"if", line, flags = re.IGNORECASE)
                # suspensions
             #  line = re.sub('[ā]',"am", line, flags = re.IGNORECASE)
                line = re.sub('mān', "mann", line, flags = re.IGNORECASE)
                line = re.sub('mann', "man", line, flags = re.IGNORECASE)
                line = re.sub('drāmys',"drammys", line, flags =re.IGNORECASE)
                line = re.sub('[ē]',"em", line, flags = re.IGNORECASE)
                line = re.sub('[ī]',"im", line, flags = re.IGNORECASE)
                line = re.sub('[ū]',"um", line, flags = re.IGNORECASE)
                line = re.sub('sōe', "some", line, flags = re.IGNORECASE)
                line = re.sub('cōmaundement',"commaundement", line, flags = re.IGNORECASE)
                line = re.sub('cōmunycacyon',"communycacyon", line, flags = re.IGNORECASE)
                line = re.sub('cōmyn',"commyn", line, flags = re.IGNORECASE)
                line = re.sub('cōpare',"compare", line, flags = re.IGNORECASE)
                line = re.sub('cōmyng',"commyng", line, flags = re.IGNORECASE)
                line = re.sub('cōtrey',"contrey", line, flags = re.IGNORECASE)
                line = re.sub('cōpellyth',"compellyth", line, flags = re.IGNORECASE)
                line = re.sub('cōnyngly',"connyngly", line, flags = re.IGNORECASE)
                line = re.sub('cōtynuannce',"contynuannce", line, flags = re.IGNORECASE)
                line = re.sub('cōuey',"conuey", line, flags = re.IGNORECASE)
                line = re.sub('cōclusyon',"conclusyon", line, flags = re.IGNORECASE)
                line = re.sub('cōfort',"comfort", line, flags = re.IGNORECASE)
                line = re.sub('cōmith',"commyth", line, flags = re.IGNORECASE)
                line = re.sub('cōperison', "comperison", line, flags = re.IGNORECASE)
                line = re.sub('cōmyst', "commyst", line, flags = re.IGNORECASE)
                line = re.sub('cōmyth', "commyth", line, flags = re.IGNORECASE)
                line = re.sub('cōmen', "commen", line, flags = re.IGNORECASE)
             #  line = re.sub('cōmoditees', "commodytees", line, flags = re.IGNORECASE)
             #  line = re.sub('cōmodytees', "commodytees", line, flags = re.IGNORECASE)
             #  line = re.sub('((?<!c)ō)',"om", line, flags = re.IGNORECASE)
             #  line = re.sub('((?<=c)ō)',"on", line, flags = re.IGNORECASE)
                line = re.sub('cōsideryng', "consideryng", line, flags = re.IGNORECASE)
                line = re.sub('cōtynuaunce', "contynuaunce", line, flags = re.IGNORECASE)
             #  line = re.sub('',"pir", line, flags = re.IGNORECASE)
             #  line = re.sub('aue',"ave", line, flags = re.IGNORECASE) #haue to have
             #  line = re.sub('eue',"eve", line, flags = re.IGNORECASE) #euer to ever
             #  line = re.sub('((?<=[aeiou])i(?=[aeiou]))',"j", line, flags = re.IGNORECASE) # unused
             #  line = re.sub('((?<=[aeiou])u(?=[aeiou]))',"v", line, flags = re.IGNORECASE)
                Output.write(line)


if __name__ == '__main__':
    main()
