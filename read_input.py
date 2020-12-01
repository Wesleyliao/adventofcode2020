def read_file(filename='input.txt'):
    with open(filename, "r") as f:
        lines = list(f.readlines())
    return lines
    