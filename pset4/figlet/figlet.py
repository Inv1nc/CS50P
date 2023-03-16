from pyfiglet import Figlet
from sys import argv, exit

if len(argv) != 3:
    exit("Invalid Usage")
figlet = Figlet()
if (argv[1] not in ['-f', '--font']):
    exit("Invalid Usage")
if (argv[2] not in figlet.getFonts()):
    exit("Invalid Usage")
figlet.setFont(font=argv[2])
s = input()
print(figlet.renderText(s))