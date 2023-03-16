# Adieu, adieu, to
def main():
    song = get_adieu()
    print(song)


def get_adieu():
    name = "Adieu, adieu, to "
    names = []
    while True:
        try:
            names.append(input())
        except EOFError:
            if len(names) == 1:
                return name+names[0]
            elif len(names) == 2:
                return name+names[0]+" and "+names[1]
            else:
                for n in range(len(names)-1):
                    name = name + names[n] + ", "
                return name + "and "+names[-1]


if __name__ == "__main__":
    main()