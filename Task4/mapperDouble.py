#!/usr/bin/env python

import sys
import re


def read_input(file):
    for line in file:
        # split the line into couples
        unpunct_line = re.sub(r'\W', ' ', line.lower())
        words = unpunct_line.split()
        yield ["{} {}".format(words[i - 1], words[i]) for i in range(1, len(words))]


def main(separator='\t'):
    # input comes from STDIN (standard input)
    data = read_input(sys.stdin)
    for triplets in data:
        for triplet in triplets:
            print '{}{}{}'.format(triplet, separator, 1)


if __name__ == "__main__":
    main()
