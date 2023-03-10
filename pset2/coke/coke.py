def main():
    amountDue = 50
    print("Amount Due:", amountDue)
    changeOwn = insertCoin(amountDue)
    print("Change Owed:", -changeOwn)


def insertCoin(amountDue):
    coins = [25, 10, 5]
    while True:
        insert = int(input("Insert Coin: "))
        # Chek insert coin is 25, 10, 5
        if insert in coins:
            amountDue = amountDue - insert
        if amountDue <= 0:
            return amountDue
        print("Amount Due:", amountDue)


main()