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
    words = ['{per}suade', 'am{per}sand', 'su{per}']
    for word in words:
        if re.match(r'{\w+}\w+', word):
            word = re.sub(r'{(\w+)}(\w+)', '\\1\\2', word)
            print(word)
        if re.match(r'\w+{\w+}\w+', word):
            word = re.sub(r'(\w+){(\w+)}(\w+)', '\\1\\2\\3', word)
            print(word)
        if re.match(r'\w+{\w+}', word):
            word = re.sub(r'(\w+){(\w+)}', '\\1\\2', word)
            print(word)
if __name__ == '__main__':
    main()
