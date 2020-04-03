# - 3.1.2.1 Required Parameters and Help Flag

# Build a CLI Tool
# Specifications:
#   Requires a filename argument so it knows what file to read.
#   Print the contents of the file backward (bottom of the script first, each line printed backward)
#   Provides help text and documentation when it receives the –help flag.
#   Accepts an optional –limit or -l flag to specify how many lines to read from the file.
#   Accepts a –version flag to print out the current version of the tool.

import argparse
import sys

# parser = argparse.ArgumentParser()

# # making the positional argument as flag makes it optional
# # metavar="" makes it more cleaner on the help documentation
# parser.add_argument("-f", "--filename", metavar="", help='file to read')

# args = parser.parse_args()

# print(args)

# — 3.1.2.3 Optional Parameters

parser = argparse.ArgumentParser(description="Basahin ang file ng pabaliktad.")
parser.add_argument("filename", help="Ang file na kailangan basahin")
parser.add_argument("-l", "--limit", type=int, help="Bilang ng linyang kailangan basahin")

parser.add_argument('-v', '--version', action='version', version='%(prog)s 1.0')

args = parser.parse_args()

try:
    f = open(args.filename)
    limit = args.limit
except FileNotFoundError as err:
    print(f"Error: {err}")
    sys.exit(1)
else:
    with f:
        lines = f.readlines()
        lines.reverse()

        if args.limit:
            lines = lines[:args.limit]

        for line in lines:
            print(line.strip()[::-1])