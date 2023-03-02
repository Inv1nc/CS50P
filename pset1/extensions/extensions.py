# Ask user for input
user = input("File name: ").strip().lower()

# Check input contain "." or not
if "." in user:
	user, dot, extension = user.rpartition(".")
else:
	extension = ""
	
# Check the extension
match extension:
	case "jpg" | "jpeg":
		print("image/jpeg")
	case "pdf":
		print("application/pdf")
	case "gif":
		print("image/gif")
	case "png":
		print("image/png")
	case "zip":
		print("application/zip")
	case "txt":
		print("text/plain")
	case "bin":
		print("application/octet-stream")
	case _:
		print("application/octet-stream")
