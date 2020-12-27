import os

# Let us print the files in the directory in which you are running this script
print(os.listdir("."))

# Let us check if this file is indeed a file!
print(os.path.isfile("./ex.py"))

# Does the file end with .py?
print("./ex.py".endswith(".py"))


def find_files_rec(suffix, path, output):
    print('rec', path)
    for file in os.listdir(path):
        file = os.path.join(path, file)
        print('in', file)
        if os.path.isfile(file) and file.endswith(suffix):
            print('append', file)
            output.append(file)
        elif os.path.isdir(file):
            output = find_files_rec(suffix, file, output)
    return output


def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    output= []
    output = find_files_rec(suffix, path, output)
    return output


path = '/Users/pierluca/Desktop/testdir'
suffix = '.c'
print(find_files(suffix, path))