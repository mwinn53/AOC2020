"""Advent of Code 2020 Day 1: Report Repair.

Parse a line and find occurrences of a character in each string

arguments: input file name

"""
from argparse import ArgumentParser as ArgParser
import progressbar

description = ('Advent of Code Day 2 problem.')
parser = ArgParser(description=description)
try:
  parser.add_argument = parser.add_option
except AttributeError:
  pass

parser.add_argument('ifname', help='Input filename.')
args = parser.parse_args()

with open(args.ifname, 'r') as f:
    lines = f.read().split('\n')


bar = progressbar.ProgressBar(maxval=len(lines), widgets=['Working... ', progressbar.Bar('=', '[', ']'), ' ', progressbar.Percentage()])
bar.start()
i = 0
count = 0
for line in lines:
    line = line.split()
    r = list(map(int, line[0].split('-')))
    if line[2].count(line[1].replace(':','')) in range(r[0],r[1]+1):
        count+=1
    i+=1
    bar.update(i)
bar.finish()
print('There are {} passwords in compliance with part 1.'.format(count))

count = 0
i=1
for line in lines:
    line = line.split()
    r = list(map(int, line[0].split('-')))

    if(len(line[2]) >= max(r)):
        r = [n - 1 for n in r]  # decrement list by 1 to account for zero-index

        # print('[{}]\tChecking {} (length {}).\t\t'.format(i, line[2], len(line[2])),str.upper(line[1].replace(':', '')), r[0] + 1, r[1] + 1)
        if (line[2][r[0]]  == line[1].replace(':','')) != (line[2][r[1]]  == line[1].replace(':','')):
            # line[2] = line[2][0:r[0]] + str.upper(line[2][r[0]]) + line[2][r[0]+1:]
            # line[2] = line[2][0:r[1]] + str.upper(line[2][r[1]]) + line[2][r[1]+1:]
            # print('\t!!! [{}]\tFound {} (length {}).\t\t'.format(i, line[2], len(line[2])), str.upper(line[1].replace(':','')),r[0]+1, r[1]+1)
            count+=1
    i+=1
print('There are {} passwords in compliance with part 2.'.format(count))