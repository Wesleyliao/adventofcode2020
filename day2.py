from read_input import read_file

lines = read_file('input2.txt')

# Part 1
valid = 0
for line in lines:
    part1, part2, part3 = line.split(' ')
    lower, upper = part1.split('-')
    target = part2[0]
    
    counts = part3.count(target)
    if int(lower) <= counts <= int(upper):
        valid += 1

print(valid)

# Part 2
valid = 0
for line in lines:
    part1, part2, part3 = line.split(' ')
    lower, upper = part1.split('-')
    target = part2[0]
    
    if (part3[int(lower)-1] == target) ^ (part3[int(upper)-1] == target):
        valid += 1

print(valid)