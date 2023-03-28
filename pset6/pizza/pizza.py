import sys
import csv
from tabulate import tabulate
if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
elif not sys.argv[1].endswith('.csv'):
    sys.exit("Not a CSV file")
data = []
try:
    file = open(sys.argv[1])
    table = csv.DictReader(file)
    print(tabulate(table, headers="keys", tablefmt="grid"))
except FileNotFoundError:
    sys.exit("File does not exist")