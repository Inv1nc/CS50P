with open("student.csv","r") as file:
    for line in file:
        student,house = line.rstrip().split(",")
        print(f"{student} is in {house}")