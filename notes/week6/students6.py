import csv
students = []

with open("names.txt","r") as file:
    reader = csv.reader(file)
    for row in reader:
        students.append({"name":row[0],"house":row[1]})

for student in students:
    print(f"{student['name']} is lives in {student['house']}")