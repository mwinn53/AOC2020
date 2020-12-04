"""Advent of Code 2020 Day 1: Report Repair.

Parse a line and find occurrences of a character in each string

arguments: input file name

"""
from argparse import ArgumentParser as ArgParser
import progressbar
import os.path

description = ('Advent of Code Day 3 problem.')
parser = ArgParser(description=description)
try:
  parser.add_argument = parser.add_option
except AttributeError:
  pass

parser.add_argument('--ifname', default=os.path.splitext(os.path.basename(__file__))[0] + 'Input.txt', help='Input filename.')
args = parser.parse_args()

def toboggan(input, over, down):
    bar = progressbar.ProgressBar(maxval=len(input), widgets=['Working... ', progressbar.Bar('-', '[',']'), ' ',progressbar.Percentage()])
    bar.start()
    i = 0
    count = 0
    tree = None
    pos = over
    print('>\tSlope = {} right, {} down'.format(over, down))
    # print('Line {}\t{}\t\t{}'.format(1, input[0], pos))
    for line in input[down::down]:  ## Skip the first line, iterates by "down"
        if line[pos] == '.':
            line = line[:pos] + 'O' + line[pos + 1:]
            tree = False
        elif line[pos] == '#':
            line = line[:pos] + 'X' + line[pos + 1:]
            count += 1
            tree = True

        # print('Line {}\t{}\t\t{}\tTree {}\tCount: {}'.format(i+down, line, pos, tree, count))
        pos = (pos + over) % len(line)
        i += down
        bar.update(i)
    bar.finish()
    return (count)


with open(args.ifname, 'r') as f:
    lines = f.read().split('\n')

total = 1
paths = [(3,1),(1,1),(5,1),(7,1),(1,2)]

for t in paths:
    n = toboggan(lines, t[0], t[1])
    total = total * n
    print('There are {} trees in the path; total of {}'.format(n, total))
