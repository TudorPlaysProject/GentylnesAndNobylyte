#!/usr/local/bin/python3
# Paul Evans (pevans@sandiego.edu)
# 9 November 2018
def main():
    with open('./input.txt', 'r') as input,\
      open('./output0.txt', 'w') as output:
        lines = input.readlines()
        for line in lines:
            output.write(line)
        
    with open('./input.txt', 'r') as input,\
      open('./output1.txt', 'w') as output:
        file = input.read()
        output.write(file)
    
if __name__ == '__main__':
    main()
