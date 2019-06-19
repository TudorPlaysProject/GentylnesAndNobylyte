#!/usr/local/bin/python3
# Paul Evans
# 19 June 2019
import re
import sys
def main():
    lines = sys.stdin.readlines()
    for line in lines:
        # includes "wtall" but does not include "thoroughowt" and "dowt"
        line = re.sub(r'\bwt',"with", line, flags = re.IGNORECASE)
        # includes "wythout" and "wythstandyng"
        line = re.sub(r'wyth',"with", line, flags = re.IGNORECASE)
        sys.stdout.write(line)

if __name__ == '__main__':
    main()
