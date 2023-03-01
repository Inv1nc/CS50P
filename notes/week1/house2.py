name = input("What's your name? ")

match name:
	case "Harry" | "Ron":
		print("Gryffindor")
	case "Hermione":
		print("Gryffindor")
	case "Drace":
		print("Slytherin")
	case _:
		print("Who?")
