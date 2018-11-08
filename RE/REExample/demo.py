#!/usr/local/bin/python3
# Paul Evans (pevans@sandiego.edu)
# 8 November 2018
import re
def main():
    f = open('./input.txt', 'r')
    lines = f.readlines()
    f.close()
    for line in lines:
        print(line)

    f = open('./input.txt', 'r')
    file = f.read()
    f.close()
    print(file)
    words = re.split('\W', file)
    for word in words:
        print(word)

    with open('./input.txt', 'r') as f:
        lines = f.readlines()
        for line in lines:
            print(line)
        
    with open('./input.txt', 'r') as f:
        file = f.read()
        words = re.split('\W', file)
        for word in words:
            print(word)
    
if __name__ == '__main__':
    main()
