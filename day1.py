from read_input import read_file

lines = [int(line) for line in read_file()]

# Part 1
def find_pair(lines, target):
    d = {}
    for num in lines:
        if target - num in d:
            return num * (target-num)
            break
        else:
            d[num] = 1
    return None
print(find_pair(lines, 2020))

# Part 2
sorted_nums = sorted(lines)
n = len(sorted_nums)
for i in range(n):
    tmp = find_pair(sorted_nums[i:], 2020-sorted_nums[i])
    if tmp:
        print(sorted_nums[i]*tmp)
