from read_input import read_file
import re
from functools import lru_cache 

lines = read_file('input10.txt')

# Part 1
def process(lines):
    
    nums = [int(line) for line in lines]
    num_set = set(nums)
    max_num = max(nums)
    
    counts = [0]*4
    curr, prev = 1, 0
    while curr - prev <= 3:
        if curr in num_set:
            # print('found match', curr, prev)
            counts[curr-prev] += 1
            prev, curr = curr, curr + 1
        else:
            curr += 1
    counts[3] += 1
    print(counts)
    print(counts[3]*counts[1])
    
process(lines)
        
# Part 2
def construct_adj(lines):
    
    nums = {int(line) : [] for line in lines}
    max_num = max(nums.keys())
    nums[max_num + 3] = []
    nums[0] = []
    
    for num in nums.keys():
        for i in range(1, 4):
            if num + i in nums:
                nums[num].append(num + i)
    
    # print('adj list', nums)
    return nums, max_num

@lru_cache()
def dfs(node, target):
    
    total = 0
    if node == target: return 1
    
    for i in range(1, 4):
        neigh = node + i
        if neigh in adj_list[node]:
            total += dfs(neigh, target)
    
    return total 


adj_list, target = construct_adj(lines)
print(dfs(0, target))