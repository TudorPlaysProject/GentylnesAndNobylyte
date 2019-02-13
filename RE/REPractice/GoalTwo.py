#!/usr/local/bin/python3
# Jordan Matuszewski
# 13 November 2018

import re 
def main():
    with open('WordListBefore.txt', 'r') as f,open('WordListAfter.txt', 'w') as output:
        file = f.read()
        words = re.split('\W', file)
        RegexOne = re.compile(r'(([a-z])*y([a-z])*)') #MatchesAllYWords
        RegexTwo= re.compile(r'([aeiou])+u/*([aeiou])') #MatchesAnyWordWithUInsteadOfV
        for word in words:
            match = RegexOne.search(word)
            matchTwo = RegexTwo.search(word)
            if match:
                # NewText.write(format(match.group(0)))
                output.write(re.sub('y','i',word))
            if matchTwo:
                # NewText.write(format(matchTwo.group(0))) 
                output.write(re.sub('u', 'v', word))        
	    if not match or not matchTwo:
	        output.write(word)
        

if __name__ == '__main__':
    main()
