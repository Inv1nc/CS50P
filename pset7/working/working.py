import re


def main():
    print(convert(input("Hours: ")))


def convert(s):
    if time:= re.match(r"^(\d{1,2}):?(\d{2})? (AM|PM) to (\d{1,2}):?(\d{2})? (AM|PM)$",s):
        start_hour, start_min, start_ap, end_hour, end_min, end_ap = time.groups()
        if start_min is None and end_min is None:
            start_min, end_min = 0, 0
        start_hour, start_min, end_hour, end_min = map(int, [start_hour, start_min, end_hour, end_min])
        if start_ap == "PM" and start_hour != 12:
            start_hour += 12
        elif start_ap == "AM" and start_hour == 12:
            start_hour = 0

        if end_ap == "PM" and end_hour != 12:
            end_hour += 12
        elif end_ap == "AM" and end_hour == 12:
            end_hour == 0

        if ( not 0 <= start_hour <= 23 or not 0 <= start_min <= 59 or not 0 <= end_hour <= 23 or not 0 <= end_min <= 59):
            raise ValueError("Invalid arguments")

        return f"{start_hour:02d}:{start_min:02d} to {end_hour:02d}:{end_min:02d}"
    raise ValueError("Invalid arguments")


if __name__ == "__main__":
    main()
