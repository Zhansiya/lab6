import os

path = input()
if os.path.exists(path) and os.access(path, os.W_OK):
    os.remove(path)
    print("File deleted.")
else:
    print("No access or file does not exist.")
