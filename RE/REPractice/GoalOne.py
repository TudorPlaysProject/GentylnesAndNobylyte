#!/usr/local/bin/python3

import re 

def main():
    OrigText = open("WordListBefore.txt", "r")
    NewText = open("WordListAfter.txt", "w")
    line = OrigText.readline()
    RegexOne = re.compile(r'(([a-z])*y([a-z])*)') #MatchesAllYWords
    RegexTwo= re.compile(r'([aeiou])+u/*([aeiou])') #MatchesAnyWordWithUInsteadOfV

    while line: 
        match = RegexOne.search(line)
        matchTwo = RegexTwo.search(line)
        if match:
            print format(match.group(0))
            print re.sub('y','i',line)
        if matchTwo:
            print format(matchTwo.group(0)) 
            print re.sub('u', 'v', line)        
	line = OrigText.readline()
    OrigText.close()
    NewText.close()

if __name__ == '__main__':
    main()
