# - 3.1.1 Accepting Simple Positional Arguments (using sys.argv)

import sys

# running script without arguments gives an IndexError if it expects an argument
# but will return the file itself including the extension if it does not expect any args
# argparse is used to provide flags/named args/help text

print(f"Positional arguments: {sys.argv[1:]}")
print(f"First argument: {sys.argv[1]}")