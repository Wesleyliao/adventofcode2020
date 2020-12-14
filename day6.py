from read_input import read_file

lines = read_file('input6.txt')

# Part 1
def count_total(lines):

    lines = ''.join(lines)
    groups = [x.split('\n') for x in lines.split('\n\n')]
    
    
    total = 0
    for group in groups:
        d = set(list(group[0]))
        for person in group:
            # print(person)
            # d = d.union(list(person))
            d = d.intersection(list(person))
        # print(list(d))
        total += len(d)
    
    print(total)
    
count_total(lines)