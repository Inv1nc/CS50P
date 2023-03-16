from random import randint


while True:
    try:
        level = int(input("Level: "))
        secretnum = randint(1, level)
        guess = int(input("Guess: "))
        if guess < secretnum:
            print("Too small!")
        elif guess > secretnum:
            print("Too large!")
        else:
            print("Just right!")
            break
    except ValueError:
        pass