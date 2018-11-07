#!/usr/local/bin/python3

import re 

def main():
    OrigText = open("WordListBefore.txt", "r")
NewText = open("WordListAfter.txt", "w")
line = OrigText.readline()

RegexOne = re.compile(r'(([A-Z])*y)') #MatchesAllYWords
RegexTwo= re.compile(r'([aeiou])+u/*([aeiou])') #MatchesAnyWordWithUInsteadOfV

while line: 
    match = RegexOne.search(line)
    matchTwo = RegexTwo.search(line)
    if match:
         printNewText(match)
    if matchTwo:
         printNewText(matchTwo) 

OrigText.close()
NewTest.close()

if __name__ == '__main__':
  main()
