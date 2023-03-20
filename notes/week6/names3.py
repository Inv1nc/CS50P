# Appending each name into the file
name = input("What's your name? ")
file = open("names.txt",'a')
file.write(f"{name}\n")
file.close()