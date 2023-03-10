# Ask user for input
camel = input("camel Case: ")
snake = ""
for i in camel:
    if i.isupper():
        snake = snake+"_"+i.lower()
    else:
        snake = snake + i
print("snake_case:", snake)