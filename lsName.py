#!/usr/bin/python3


import commands
# uses the ls command in linux to show whats in folder 
output = commands.getoutput('ls')
print output

#prints out the number of d are in there in folder 
num = output.count('d')
print num
