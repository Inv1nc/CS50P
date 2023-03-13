months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
]


def main():
    date = get_date()
    print(date)


def get_date():
    while True:
        date = input("Date: ")
        try:
            if len(date.split("/")) == 3:
                month, day, year = map(int, date.split("/"))
                if month <= 12 and day <= 31:
                    return f"{year:04}-{month:02}-{day:02}"
            else:
                date = date.split(",")
                if len(date) == 2:
                    month, day = date[0].split()
                    month = months.index(month) + 1
                    year = int(date[1])
                    if int(month) <= 12 and int(day) <= 31:
                        return f"{year:04}-{month:02}-{day:02}"
        except ValueError:
            pass
        except (EOFError, KeyboardInterrupt):
            print()
            break


main()