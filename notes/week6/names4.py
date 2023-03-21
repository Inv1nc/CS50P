with open("names.txt","a") as file:
    for _ in range(3):
        name = input("Enter Name: ")
        file.write(f"{name}\n")