students = []
with open("student.csv","r") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        student = {"name":name, "house":house}
        students.append(student)

for student in students:
    print(f"{student['name']} is in {student['house']}")