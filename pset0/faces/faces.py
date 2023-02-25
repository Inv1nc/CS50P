# Ask input from user
user = input()

# Replace :) and :( with emojis
faces = user.replace(":)", "🙂").replace(":(", "🙁")

# Print Output
print(faces)
