# Ask user for input
user = input("Greeting: ").lower().strip()

# Check greeting condition
if user.startswith("hello"):
    print("$0")
elif user.startswith("h"):
    print("$20")
else:
    print("$100")
