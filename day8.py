from read_input import read_file
import re
from functools import lru_cache 

lines = read_file('input8.txt')

def process(lines):
    
    i = 0
    visited = set()
    acc = 0
    
    while i not in visited and i < len(lines):
        visited.add(i)
        op, arg = lines[i].split(' ')
        arg = int(arg)
        
        if op == 'nop':
            i += 1
        elif op == 'acc':
            acc += arg
            i += 1
        elif op == 'jmp':
            i += arg
        
    
    print(acc)
    
    return i == len(lines)

process(lines)

# Part 2

for i, line in enumerate(lines):
    orig = line
    if 'jmp' in line:
        lines[i] = line.replace('jmp', 'nop')
    elif 'nop' in line:
        lines[i] = line.replace('nop', 'jmp')
        
    if process(lines):
        print('SUCCESS')
        break
    
    lines[i] = orig
    

    