#!/usr/bin/python
#
# Paul Evans, Maya McAuliffe, Erin McDonald
# 6 December 2016
#
import re
import string
def main():
    sample = 'I love computer science very, very much. Nimbus 2000. Crustacean.'
    print(sample)
    sample = sample.lower() # lower case string
    print(sample)
    sample = re.sub('['+string.punctuation+']', '', sample) # strip punctuation
    print(sample)
    words = re.split('\W', sample) # split on words
    print(words)
    for word in words: # loop on words
        word = re.sub('v', 'u', word) # substitute 'u' for 'v'
        word = re.sub('us$', 'a', word) # substitute 'a' for terminal 'us'
        print(word)

if __name__ == '__main__':
    main()

