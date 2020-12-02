def read_file(filename):
    with open(filename, "r") as f:
        lines = list(f.readlines())
    return lines
    