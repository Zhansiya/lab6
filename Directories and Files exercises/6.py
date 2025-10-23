import shutil

src = input("Source file: ")
dst = input("Destination file: ")

shutil.copyfile(src, dst)
