import sys
if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
elif not sys.argv[1].endswith('.py'):
    sys.exit("Not a Python file")
count = 0
try:
    file = open(sys.argv[1])
    for line in file:
        line = line.strip()
        if line.strip() and not line.lstrip().startswith("#"):
            count += 1
except FileNotFoundError:
    sys.exit("File does not exist")
print(count)