import csv

file = open ("stars.csv" ,  "w")
newrecord = "Brian, 73, Taurus\n" 
file.write(str(newrecord))
file.close()
