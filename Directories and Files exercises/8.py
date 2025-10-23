import os

path = input()

if os.path.exists(path):
    if os.access(path, os.F_OK) and os.access(path, os.W_OK):
        os.remove(path)
        print("File deleted successfully.")
    else:
        print("No permission to delete this file.")
else:
    print("Path does not exist.")