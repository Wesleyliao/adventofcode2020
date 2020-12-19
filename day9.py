from read_input import read_file
import re
from functools import lru_cache 

lines = read_file('input9.txt')

def twosum(lst, target):
    
    d = {}
    for num in lst:
        if target-num in d:
            return True
        d[num] = 1
         
    return False

# Part 1        
def process(lines, preamble=25):
    
    lst = []
    for i, line in enumerate(lines):
        
        num = int(line)
        if i >= preamble:
            if not twosum(lst, num):
                print('Found it', num)
                break
        lst.append(num)
        if len(lst) > preamble:
            lst = lst[1:]

process(lines, 25)

# Part 2
def findrange(lines, target=15353384):
    
    l = len(lines)
    nums = [int(line) for line in lines]
    accum = [0] * l
    a, b = 0, 0
    for i, num in enumerate(nums):
        
        if i == 0:
            accum[0] = num
        else:
            accum[i] = accum[i-1] + num
        
        for j in range(0, i):
            if accum[i] - accum[j] == target:
                print('found range', nums[j+1], nums[i])
                a, b = j+1, i
        
        if a or b:
            break
    
    mn, mx = float('inf'), float('-inf')
    for i in range(a, b+1):
        mn = min(mn, nums[i])
        mx = max(mx, nums[i])
        
    print('answer', mn+mx)

findrange(lines)