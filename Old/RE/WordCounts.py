#!/usr/local/bin/python3
# Jordan Matuszewski
# 05 February 2019

import re
def main():
    file1 = open('WLBeforeHamming.txt','r').read()  
    file2 = open('X_Gentylnes_and_Nobylyte.txt').read()

    words = re.split('\W', file1)
    allWords = re.split('\W', file2)
    
    d = {}
    for word in words:
        word.strip()
        print(word)
        for anyWord in allWords:
           # print(anyWord)
            anyWord.strip()
            if word == anyWord:
                d[word] += 1
            else:
                d[word] = 1


    lst = [(d[w],w) for w in d]
    lst.sort()
    lst.reverse()
    for count, word in lst:
        print('%4s %s' %(count,word))
       
if __name__ == '__main__':
    main()
