from random import randint


def main():
    level = get_level()
    problemSet = generate_integer(level)
    score = 0

    for question in problemSet:
        incorrect = 0

        while True:
            try:
                user = int(input(f"{question} = "))
                a, b = question.strip().split('+')
                result = int(a)+int(b)
                if incorrect == 2:
                    print("EEE")
                    print(question, "=", str(result))
                    break
                elif user != result:
                    incorrect += 1
                    print("EEE")
                else:
                    score += 1
                    break
            except ValueError:
                print("EEE")
                incorrect += 1
    print("Score:", score)


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if 1 > level or level > 3:
                raise ValueError
            return level
        except ValueError:
            pass


def generate_integer(level):
    limits = {1: [0, 9], 2: [10, 99], 3: [100, 999]}
    limit1 = limits[level][0]
    limit2 = limits[level][1]
    problemSet = []
    for i in range(1, 11):
        random1 = randint(limit1, limit2)
        random2 = randint(limit1, limit2)
        problemSet.append(f"{random1} + {random2}")
    return problemSet


if __name__ == "__main__":
    main()
