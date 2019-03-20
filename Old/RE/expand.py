#!/usr/local/bin/python3
# Paul Evans
# 15 March 2019
#
# Early printed texts (c.1475-1550) inherited conventions from the
# medieval Latin manuscript tradition, including abbreviations. For
# example, a common abbreviation is a 'p' with a slash through the
# descender (U+751) for "per". EEBO-TCP, the source for the texts
# used by TPP, expands abbreviations, surrounding the expanded text
# with curly brackets. The curly brackets have to be removed from the
# text before authorship attribution analysis. This demo code shows
# how to use Python raw strings and regular expression capturing
# groups to safely remove the curly brackets.
# 
import re
def main():
    lines = ['foo bar baz {per}suade foo bar baz',
             'foo bar baz am{per}sand foo bar baz',
             'foo bar baz su{per} foo bar baz']
    for line in lines:
        # line = re.sub(r'(.*){(\w+)}(.*)', '\\1\\2\\3', line) # works
        line = re.sub(r'{(\w+)}', '\\1', line) # works!
        print(line)
if __name__ == '__main__':
    main()
