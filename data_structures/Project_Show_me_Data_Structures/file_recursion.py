import os


def find_files_rec(suffix, path, output):
    """
    recursive function to be called for output

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system
      output(list): list of path

    Returns:
       output(list):  a list of paths
    """
    for file in os.listdir(path):
        file = os.path.join(path, file)
        if os.path.isfile(file) and file.endswith(suffix):
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
    if not os.path.exists(path):
        return "unexisting path"
    output= []
    output = find_files_rec(suffix, path, output)
    return output


if __name__ == "__main__":
    # Test Case 1
    path = 'testdir'
    suffix = '.c'
    print(f"in path {path} following files have suffix {suffix}:\n {find_files(suffix, path)}")# expected 6 files

    # Test Case 2
    path = 'testdir'
    suffix = '.h'
    print(f"in path {path} following files have suffix {suffix}:\n {find_files(suffix, path)}")# expected 4 files

    # Test Case 3
    path = 'testdir/subdir1'
    suffix = '.h'
    print(f"in path {path} following files have suffix {suffix}:\n {find_files(suffix, path)}")# expected 1 files

    # Test Case 4
    path = 'testdir/subdir1'
    suffix = '.h0'
    print(f"in path {path} following files have suffix {suffix}:\n {find_files(suffix, path)}")# expected empty list

    # Test Case 5
    path = 'testdir2'
    suffix = '.h0'
    print(f"in path {path} following files have suffix {suffix}:\n {find_files(suffix, path)}")# expected  error message