import csv

row_dictionary = []
with file("AustinSol2018-stats.csv") as csv_file:
    csv_reader = csv.reader(csv_file)
    for row in csv_reader:
        row_dictionary.append(row)

print row_dictionary[0]
