#!/usr/bin/env python3

from itertools import groupby
from operator import itemgetter
import sys


def read_mapper_output(ifile, separator='\t'):
    for line in ifile:
        yield line.rstrip().split(separator, 1)


def main(separator='\t'):
    data = read_mapper_output(sys.stdin, separator=separator)
    for current_triplet, group in groupby(data, itemgetter(0)):
        try:
            total_count = sum(int(count) for current_triplet, count in group)
            print("{}{}{}".format(current_triplet, separator, total_count))
        except ValueError:
            # count was not a number, so silently discard this item
            pass


if __name__ == "__main__":
    main()
