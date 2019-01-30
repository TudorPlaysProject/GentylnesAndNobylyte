#!/usr/local/bin/python3
# Jordan Matuszewski
# 13 Janruary 2019

import re
def main():
    with open('WLBeforeHamming.txt', 'r') as f,open('WLAfterHamming.txt', 'w') as output:
        file = f.read()
        words = re.split('\W', file)
        for word in words:
            string1=word
            for otherword in words:
                string2=otherword
                if len(string1)==len(string2):
                    i=0
                    count=0
                    while i<=len(string1):
                        if string1[i]!=string2[i]:
                            count=count+1
                            i=i+1
                        if count<=1:
                            string2=''




if __name__ == '__main__':
    main()

