email = input("What's your email? ")

if '@' in email and '.' in email:
    print("Valid")
else:
    print("Invalid")