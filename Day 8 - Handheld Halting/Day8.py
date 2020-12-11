"""Advent of Code 2020 Day 8: Custom Customs

Parse a line and find occurrences of a character in each string

arguments: input file name

"""

from argparse import ArgumentParser as ArgParser
from collections import Counter
from itertools import chain
import os.path

description = ('Advent of Code Day 8 problem.')
parser = ArgParser(description=description)
try:
  parser.add_argument = parser.add_option
except AttributeError:
  pass

parser.add_argument('--ifname', default=os.path.splitext(os.path.basename(__file__))[0] + 'Input.txt', help='Input filename.')
args = parser.parse_args()

def interpreter(line):
    # returns index increment (+/-) and accumulator increment (+/-)
    l = line.split(' ')
    # print('\tLine:\t{}'.format(l))
    if l[0] == 'acc':
        return 1, int(l[1])

    if l[0] == 'jmp':
        return int(l[1]), 0

    if l[0] == 'nop':
        return 1, 0

def detectloop(lines):
    ax = 0  ## accumulator
    bx = [0] * len(lines)  ## instruction counter
    ip = 0  ## index
    result = False
    while ip != len(lines):
        if ip > len(lines):
            print('Buffer overflow')
            break
        if bx[ip] == 1:
            result = True
            break
        else:
            i, a = interpreter(lines[ip])
            bx[ip] += 1
            ip += i
            ax += a
            # print('\t\t\tIncrement the index by {} to {}\tIncrement the register by {} to {}'.format(i, ip, a, ax))
    print('\tLine {}\tLoop detected = {}. Register {}'.format(ip, result, ax))
    return result, ax

with open(args.ifname, 'r') as f:
    lines = f.read().split('\n')

# code, register = detectloop(lines)
# print('The value in the register is:\t{} Loop detected = {}'.format(register, code))

for i in range(0, len(lines), 1):
    lines2 = lines

    print('[{}]\tLine:\t\t\t{}'.format(i,lines2[i]))

    if lines2[i][0:3] == 'jmp':
        lines2[i] = lines2[i].replace('jmp', 'nop')
        print('[{}]\tNew Line:\t\t{}'.format(i, lines2[i]))
    elif lines2[i][0:3] == 'nop':
        lines2[i] = lines2[i].replace('nop','jmp')
        print('[{}]\tNew Line:\t\t{}'.format(i, lines2[i]))
    code, register = detectloop(lines2)

    if code:
        print('Loop detected. Trying again.')
    else:
        print('Successful execution. The value in the register is {}'.format(register))
        break
print('Successful execution. The value in the register is {}'.format(register))