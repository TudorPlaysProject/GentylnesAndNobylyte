#!/usr/local/bin/python3
# Paul Evans
# 30 January 2019
# This shouldn't work, but it does.
def main():
    strings = ['alpha', 'bravo', 'charlie', 'delta']
    for outer in strings:
        for inner in strings:
            print(outer, inner)

if __name__ == '__main__':
    main()
