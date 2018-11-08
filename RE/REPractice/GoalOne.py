#!/usr/local/bin/python3

import re 

def main():
    OrigText = open("WordListBefore.txt", "r")
    NewText = open("WordListAfter.txt", "w")
    lines = OrigText.readlines()
    RegexOne = re.compile(r'(([a-z])*y([a-z])*)') #MatchesAllYWords
    RegexTwo= re.compile(r'([aeiou])+u/*([aeiou])') #MatchesAnyWordWithUInsteadOfV

    for line in lines:
        match = RegexOne.search(line)
        matchTwo = RegexTwo.search(line)
        if match:
            # NewText.write(format(match.group(0)))
            NewText.write(re.sub('y','i',line))
        if matchTwo:
            # NewText.write(format(matchTwo.group(0))) 
            NewText.write(re.sub('u', 'v', line))        
    OrigText.close()
    NewText.close()

if __name__ == '__main__':
    main()
