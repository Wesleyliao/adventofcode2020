from read_input import read_file
import re
from functools import lru_cache 

lines = read_file('input7.txt')

def process(lines, target='shiny gold'):
    
    i = 0
    mapping = {}
    adj_list = {}
    cnt_list = {}
    rev_list = {}
    
    for line in lines:
        key, vals = line.split(' bags contain ')
        if 'no other bags.' not in vals:
            vals = [x.replace(' bags', '').replace(' bag', '').split(' ', 1) for x in re.split(', |\.', vals) if x not in ['\n', '']]
            
            for quant, color in vals:
                adj_list[key] = adj_list.get(key, []) + [color]
                cnt_list[key] = cnt_list.get(key, []) + [int(quant)]
                rev_list[color] = rev_list.get(color, []) + [key]
    
    # Part 1
    uniq = set()
    queue = [target]
    while queue:
        
        curr = queue.pop()
        for neigh in rev_list.get(curr, []):
            if neigh not in uniq:
                uniq.add(neigh)
                queue.append(neigh)
    
    print(len(uniq))

    # Part 2
    @lru_cache(maxsize=512)
    def dfs(root):
        
        total = 1
        if root in adj_list:
            for neigh, count in zip(adj_list[root], cnt_list[root]):
                total += count*dfs(neigh)
        
        return total
    
    print(dfs(target)-1)
        
        
process(lines)


