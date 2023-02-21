# Ask user for name
name = input("What's your name? ").title()

# Splits into first, last name
first, last = name.split(" ")
# Print
print(f"First Name: {first} \nLast Name: {last}")
