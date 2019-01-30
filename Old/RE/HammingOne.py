#!/usr/local/bin/python3
# Jordan Matuszewski
# 12 Janruary 2019

import re
def main():
    def hamming_distance(s1, s2):
        assert len(s1) == len(s2)
        return sum(ch1 != ch2 for ch1, ch2 in zip(s1, s2))

    with open('WLBeforeHamming.txt', 'r') as f,open('WLAfterHamming.txt', 'w') as output:
        file = f.read()
        words = re.split('\W', file)
        for word in words:
            s1=word
            for otherword in words:
                s2=word
                i=0
                count=0
                while s1!=' ' and s2!=' ':
                    for i in s1 and i in s2:
                        if s1[i]==



if __name__ == '__main__':
    main()

