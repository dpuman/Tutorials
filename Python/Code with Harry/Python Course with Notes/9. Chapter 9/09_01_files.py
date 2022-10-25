# Use open function to read the content of a file!
# f = open('sample.txt', 'r')
# import os
# by default the mode is r
f = open("./sample.txt")
# data = f.read()
data = f.read(5)  # reads first 5 characters from the file
print(data)
f.close()

# cwd = os.getcwd()  # Get the current working directory (cwd)
# files = os.listdir(cwd)  # Get all the files in that directory
# print("Files in %r: %s" % (cwd, files))
