"""Advent of Code 2020 Day 1: Report Repair.

Find the addends of a sum from a list and provide the product.

arguments: input file name
function: findb

"""
from argparse import ArgumentParser as ArgParser

description = ('Command line interface for enriching list of IP Addresses.')
parser = ArgParser(description=description)
try:
  parser.add_argument = parser.add_option
except AttributeError:
  pass

parser.add_argument('ifname', help='Input filename.')
args = parser.parse_args()


def findb(sum, data):
    i = 1
    for a in data:
        b = sum - a
        if b in data:
            print('  Found {} and {} at position {} after {} iterations.'.format(a, b, data.index(b), i))
            return a, b
        i += 1
    return 0, 0

year = 2020

with open(args.ifname, 'r') as f:
    lines = f.read().split('\n')

lines = list(map(int, lines))
lines.sort(reverse=True)

a, b = findb(year, lines)

print('The first solution is: {} + {} = {}'.format(a, b, a+b))
print('The first solution is: {} * {} = {}'.format(a, b, a*b))
print('---------------------------------------')

for line in lines:
    a, b = findb(year-line, lines)
    if (a + b > 0):
        print('The second solution is: {} + {} + {} = {}'.format(a, b, line, a + b + line))
        print('The second solution is: {} * {} * {} = {}'.format(a, b, line, a * b * line))
        break