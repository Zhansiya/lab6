file = input()

with open(file, 'r') as f:
    lines = f.readlines()
    print(len(lines))
