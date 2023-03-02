def main():
    # User input
    expression = input("Expression: ")
    x, y, z = expression.strip().split(" ")
    print(f"{interpreter(int(x), str(y), int(z)):.1f}")


def interpreter(x, y, z):
    # Calculation
    if y == "+":
        return x + z
    elif y == "-":
        return x - z
    elif y == "*":
        return x * z
    elif y == "/":
        return x / z


main()
