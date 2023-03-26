import csv

students = []

with open("names.txt","r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        students.append(row)

for student in students:
    print(f"{student['name']} is lives in {student['house']}")