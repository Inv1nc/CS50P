vowels = ['a', 'e', 'i', 'o', 'u']


def main():
    # Ask user for input
    user = input("Input: ")
    output = get_output(user)
    print("Output:", output)


def get_output(input):
    output = ""
    for i in input:
        # Check if it contain vowels or not
        if i.lower() in vowels:
            continue
        else:
            output = output + i
    # Return Final Output
    return output


main()