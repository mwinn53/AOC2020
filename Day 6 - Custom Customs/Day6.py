"""Advent of Code 2020 Day 6: Custom Customs

Parse a line and find occurrences of a character in each string

arguments: input file name

"""

from argparse import ArgumentParser as ArgParser
from collections import Counter
from itertools import chain
import os.path

description = ('Advent of Code Day 6 problem.')
parser = ArgParser(description=description)
try:
  parser.add_argument = parser.add_option
except AttributeError:
  pass

parser.add_argument('--ifname', default=os.path.splitext(os.path.basename(__file__))[0] + 'Input.txt', help='Input filename.')
args = parser.parse_args()

with open(args.ifname, 'r') as f:
    lines = f.read().split('\n\n')

yes = 0
for line in lines:
    yes += len(set(line.replace('\n', '')))

print('The sum of YES answers is {}'.format(yes))

yes = 0
for line in lines:
    l = line.split('\n')
    s = (set(sub) for sub in l)
    counts = Counter(chain.from_iterable(s))
    n = len([i for i in counts.values() if i == len(l)])
    yes += n
    print('There are {} complete answers in\n{}\n'.format(n, line))

print('There are {} complete answers in the set.'.format(yes))