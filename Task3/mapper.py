#!/usr/bin/env python3

import sys
import re


def read_input(ifile):
    for line in ifile:
        unpLine = re.sub(r'\W', ' ', line.lower())
        words = unpLine.split()
        yield ["{} {} {}".format(words[i - 2],
                                 words[i - 1],
                                 words[i]) for i in range(2, len(words))]


def main(separator='\t'):
    data = read_input(sys.stdin)
    for triplets in data:
        for triplet in triplets:
            print('{}{}{}'.format(triplet, separator, 1))


if __name__ == "__main__":
    main()
