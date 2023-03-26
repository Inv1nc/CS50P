import csv
students = []

with open("names.txt","r") as file:
    reader = csv.reader(file)
    for name, house in reader:
        students.append({"name":name,"house":house})

for student in students:
    print(f"{student['name']} is lives in {student['house']}")