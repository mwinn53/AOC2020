"""Advent of Code 2020 Day 9: Custom Customs

Parse a line and find occurrences of a character in each string

arguments: input file name

"""

from argparse import ArgumentParser as ArgParser
import os.path

description = ('Advent of Code Day 9 problem.')
parser = ArgParser(description=description)
try:
  parser.add_argument = parser.add_option
except AttributeError:
  pass

parser.add_argument('--ifname', default=os.path.splitext(os.path.basename(__file__))[0] + 'Input.txt', help='Input filename.')
args = parser.parse_args()

def insum(group, sum):
    for s in group:
        if s > sum:
            continue
        elif (sum - s) in group:
            return True
    return False

def findweakness(group, sum):
    i = 1
    result = group[0]
    for i in range(i, len(group), 1):
        if result > sum:
            return None
        elif result == sum:
            return min(group[0:i]), max(group[0:i]), i
        result += group[i]

with open(args.ifname, 'r') as f:
    lines = f.read().split('\n')

lines = list(map(int, lines))
i = 25

for i in range(i,len(lines),1):
    # print('Checking {}\tLines {} to {}\tfor sum {} at line {}'.format(lines[i-25:i], i-25, i-1, lines[i], i))
    if not insum(lines[i-25:i], lines[i]):
        result = lines[i]
        break

print('Successful execution. The value is {} at line {}.'.format(result, i))

i = 1

for i in range(i,len(lines),1):
    weakness = findweakness(lines[i:len(lines)], result)
    if weakness:
        break

print('The weak values are {} + {} = {} (Lines {}-{}).'.format(weakness[0], weakness[1], weakness[0] + weakness[1],i, i+weakness[2]))