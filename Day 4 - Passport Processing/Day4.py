"""Advent of Code 2020 Day 4: Passport Processing

Parse a line and find occurrences of a character in each string

arguments: input file name

"""
from argparse import ArgumentParser as ArgParser
import progressbar
import os.path
import re

description = ('Advent of Code Day 4 problem.')
parser = ArgParser(description=description)
try:
  parser.add_argument = parser.add_option
except AttributeError:
  pass

parser.add_argument('--ifname', default=os.path.splitext(os.path.basename(__file__))[0] + 'Input.txt', help='Input filename.')
args = parser.parse_args()

with open(args.ifname, 'r') as f:
    lines = f.read().split('\n\n')

def checkline(line, schema):
    result = True
    line = line.replace('\n', ' ')
    d = dict(x.split(':') for x in line.split(' '))
    print('\tChecking {}'.format(d))
    for s in schema:
        if s in d:
            result = result and validateline(s, d)
        else:
            result = False
        if not result:
            if s in d:
                print('\tline is invalid because {} is {}....breaking'.format(s, d[s]))
                pass
            else:
                print('\tline is invalid because {} is not present....breaking'.format(s))
                pass
            break
        print('\t\t{}:{} is valid'.format(s,d[s]))
    return result

def validateline(field, line):
    if field == 'byr':
        return int(line[field]) in range(1920,2002+1)   # +1 includes the last number in the range
    elif field == 'iyr':
        return int(line[field]) in range(2010, 2020+1)
    elif field == 'eyr':
        return int(line[field]) in range(2020, 2030+1)
    elif field == 'hgt':
        if str(line[field])[-2:] == 'cm':
            return int(line[field][0:len(str(line[field])) - 2]) in range(150, 193+1)
        elif str(line[field])[-2:] == 'in':
            return int(line[field][0:len(str(line[field])) - 2]) in range(59, 76+1)
        else:
            return False
    elif field == 'hcl':
        return bool(re.match(r'^#([0-9a-f]{6})', line[field]))
    elif field == 'ecl':
        return bool(re.match(r'^(amb|blu|brn|gry|grn|hzl|oth){1}', line[field]))
    elif field == 'pid':
        return bool(re.match(r'^[0-9]{9}', line[field]))
    else:
        return False

schema = ['byr', 'iyr', 'eyr','hgt','hcl','ecl','pid']
## NOTE: cid is optional

count = 0
for passport in lines:
    if checkline(passport, schema):
        count += 1
        print('Count is now {}'.format(count))
    else:
        print('Count stays at {}'.format(count))

print('There are {} valid passports.'.format(count))