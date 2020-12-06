"""Advent of Code 2020 Day 5: Binary Boarding

Parse a line and find occurrences of a character in each string

arguments: input file name

"""
from argparse import ArgumentParser as ArgParser
import progressbar
import os.path
import re

description = ('Advent of Code Day 5 problem.')
parser = ArgParser(description=description)
try:
  parser.add_argument = parser.add_option
except AttributeError:
  pass

parser.add_argument('--ifname', default=os.path.splitext(os.path.basename(__file__))[0] + 'Input.txt', help='Input filename.')
args = parser.parse_args()

def checkrow(row):
    row = row[0:7]
    row = row.replace('F','0')
    row = row.replace('B', '1')

    return int(row, base=2)

def checkcol(row):
    row = row[7:10]
    row = row.replace('L', '0')
    row = row.replace('R', '1')

    return int(row, base=2)

with open(args.ifname, 'r') as f:
    lines = f.read().split('\n')

maxid = 0
for line in lines:
    boardingid = (checkrow(line) * 8) + checkcol(line)
    if boardingid > maxid:
        maxid = boardingid

print('The highest Seat ID is {}'.format(maxid))

seatlist = []
for line in lines:
    seatlist.append(checkrow(line) * 8 + checkcol(line))

seatlist = sorted(seatlist)

print('Seat IDs that did not check in: {}'.format([x for x in range(seatlist[0], seatlist[-1]+1)  if x not in seatlist]))