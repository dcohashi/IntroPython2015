#!/usr/bin/env python3

infile =  open('testfile.txt','r')
outfile = open('copyfile.txt', 'w')
while True:
    line = infile.readline()
    if  not line:
       outfile.close()
       break 
    outfile.write(line)
