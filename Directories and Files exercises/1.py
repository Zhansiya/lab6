import os

path = input().strip('"')

print("Directories:")

for i in os.listdir(path):
    if os.path.isdir(os.path.join(path,i)):
        print(i)

print("Files:")
for i in os.listdir(path):
    if os.path.isfile(os.path.join(path, i)):
        print(i)

print("All:")
for i in os.listdir(path):
    print(i)
