import csv

with open("students.csv", "r") as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)
        print(row[0])
        print(row[1])
        print(row[2])