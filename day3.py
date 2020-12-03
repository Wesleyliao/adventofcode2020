from read_input import read_file

lines = read_file('input3.txt')

# Part 1
def part1(lines, hori, vert):
    j = 0
    trees = 0
    n = len(lines[0])-1
    for i, line in enumerate(lines):
        if (i % vert) == 0:
            j = ((i // vert)*hori) % n
            # print('line', i, j, line[j] == '#')
            if line[j] == '#':
                trees += 1
    print(trees)
    return trees

# Part 2
print(
    part1(lines, 1, 1)*part1(lines, 3, 1)*part1(lines, 5, 1)*part1(lines, 7, 1)*part1(lines, 1, 2)
)