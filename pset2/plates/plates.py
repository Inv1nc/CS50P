def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    values = [" ", "?", "."]
    flag = True
    # Vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters
    if not (2 <= len(s) <= 6):
        return False
    # All vanity plates must start with at least two letters.
    elif not (s[0].isalpha() and s[1].isalpha()):
        return False
    # No periods, spaces, or punctuation marks are allowed
    for i in s:
        if i in values:
            return False

    for char in s:
        if char.isnumeric():
            first_num = s.index(char)
            # The first number used cannot be a '0'
            if char == '0':
                return False
            # Numbers cannot be used in the middle of a plate
            for char in s[first_num:]:
                if char.isalpha():
                    return False
            break
    return True


main()