#!/usr/local/bin/python3
# Paul Evans
# 19 June 2019
import re
def main():
    with open('input.txt', 'r') as infile, open('output.txt', 'w') as outfile:
        lines = infile.readlines()
        for line in lines:
            # includes "wtall" but does not include "thoroughowt" and "dowt"
            line = re.sub(r'\bwt',"with", line, flags = re.IGNORECASE)
            # includes "wythout" and "wythstandyng"
            line = re.sub(r'wyth',"with", line, flags = re.IGNORECASE)
            outfile.write(line)

if __name__ == '__main__':
    main()
