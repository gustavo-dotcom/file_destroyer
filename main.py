import fnmatch
import os


def find(pattern, path):
    for root, dirs, files in os.walk(path):
        for name in files:
            if fnmatch.fnmatch(name, pattern):
                files_found.append(os.path.join(root, name))
    return files_found


# file_name needs to contain one word or the full name of the file to be deleted
# for example, if you want to delete all png files: "*.png"
files_name = input("File name: ")
# the file_path doesn't need to be the exact path where the file(s) is, but be careful
# because this script could delete files from all directories forward the path
file_path = input("File path: ")
files_found = []
find(files_name, file_path)
for file in files_found:
    os.remove(file)
