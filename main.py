import sys

if len(sys.argv) != 2:
	print ("Usage: python3 main.py <path_to_book>")
	sys.exit(1)

from stats import wcount

from stats import count_characters

from stats import make_report

make_report()
