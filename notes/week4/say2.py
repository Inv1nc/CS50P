import sys

from sayings import hello

if len(sys.argv) == 2:
    print(hello(sys.argv[1]))