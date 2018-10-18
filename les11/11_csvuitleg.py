import csv

with open("gamers.csv", 'r')as myCSvFile:
    reader = csv.reader(myCSvFile, delimiter=';')
    for row in reader:
        print(row[0], row[2])
# met kolomkoppen is het csv.dictreader
