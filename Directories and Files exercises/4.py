items = ['apple', 'banana', 'cherry']
file = input()

with open(file, 'w') as f:
    for i in items:
        f.write(i + '\n')
