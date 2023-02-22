def main():
    name = input("What's your name? ")
    print(f"Hii {name}\nI am Calculator")
    operation = input("1.Addition\n2.Subtraction\n3.Multiplication\n4.Dvision\nSelect the option(1/2/3/4): ")
    x = float(input("What's X? "))
    y = float(input("What's y? "))
    if operation == '1':
        return add(x,y)
    elif operation == '2':
        return sub(x,y)
    elif operation == '3':
        return multiply(x,y)
    elif operation == '4':
        return divide(x,y)

def add(x,y):
    print(int(x+y))
def sub(x,y):
    print(int(x-y))
def multiply(x,y):
    print(x*y)
def divide(x,y):
    print(x/y)
main()
