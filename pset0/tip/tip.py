# Main Function
def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    # TODO
    dollar = float(d.lstrip("$"))
    return dollar


def percent_to_float(p):
    # TODO
    percent = float(p.removesuffix("%"))
    percent = percent / 100
    return percent


main()

