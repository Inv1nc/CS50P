from emoji import emojize
# Ask user for input
user = input("Input: ")
txt_emoji = emojize(user, language='alias')
print("Output:", txt_emoji)