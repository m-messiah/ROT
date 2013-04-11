#!/usr/bin/env python

from itertools import groupby
from operator import itemgetter
import sys


def read_mapper_output(file, separator='\t'):
    for line in file:
        yield line.rstrip().split(separator, 1)


def main(separator='\t'):
    # input comes from STDIN (standard input)
    data = read_mapper_output(sys.stdin, separator=separator)
    for current_unit, group in groupby(data, itemgetter(0)):
        try:
            total_count = sum(int(count) for current_unit, count in group)
            print "{}{}{}".format(current_unit, separator, total_count)
        except ValueError:
            # count was not a number, so silently discard this item
            pass


if __name__ == "__main__":
    main()
