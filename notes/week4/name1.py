import sys

try:
    print("Hello,",sys.argv[1])
except IndexError:
    print("Too few arguments")