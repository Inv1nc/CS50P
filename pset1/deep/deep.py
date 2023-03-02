# Ask input from user
user = input("What is the Answer to the Great Question of Life, the Universe and Everything? ")
user = user.lower().strip().replace("-", " ")

# Check whether input is 42 or not
match user:
    case "42" | "forty two":
        print("Yes")
    case _:
        print("No")
