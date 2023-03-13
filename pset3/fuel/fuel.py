# Fuel Guage Indication
def main():
    fraction = int(get_fuel())
    if fraction == 0:
        print("E")
    elif fraction == 1:
        print("F")
    else:
        print(f"{fraction}%")


def get_fuel():
    while True:
        try:
            # Taking input from user
            x, y = input("Fraction: ").split("/")
            # Return the fraction
            return (float(x)/float(y))*100
        except (ValueError, ZeroDivisionError):
            pass


main()