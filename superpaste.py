__version__ = 0.1

import sys

def main():

    # Get filenames
    f1, f2 = sys.argv[1], sys.argv[2]

    # Read all of file 1 and figure out max line width
    fp = open(f1, "r")
    f1lines = fp.readlines()
    fp.close()
    f1width = max([len(line) for line in f1lines])

    # Read all of file 2 and figure out max line width
    fp = open(f2, "r")
    f2lines = fp.readlines()
    fp.close()
    f2width = max([len(line) for line in f2lines])

    # Extend shortest file with blank lines
    if len(f1lines) > len(f2lines):
        f2lines.extend(["",]*(len(f1lines) - len(f2lines)))
    else:
        f1lines.extend(["",]*(len(f2lines) - len(f1lines)))

    # Print lines side by side, with padding for legibility
    for f1line, f2line in zip(f1lines, f2lines):
        print f1line.strip().ljust(f1width) + " "*8 + f2line.strip()
    fp.close()
