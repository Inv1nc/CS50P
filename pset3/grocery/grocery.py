def main():
    dict = get_dict()
    for item, count in sorted(dict.items()):
        print(f"{count} {item}")


def get_dict():
    dict = {}
    while True:
        try:
            item = input().upper()
        except (EOFError, KeyboardInterrupt):
            print()
            return dict
        else:
            if item in dict:
                dict[item] += 1
            else:
                dict[item] = 1


main()