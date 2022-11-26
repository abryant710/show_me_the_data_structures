"""
Finding Files
For this problem, the goal is to write code for finding all files under a directory (and all directories beneath it) that end with ".c"

Here is an example of a test directory listing, which can be downloaded here (https://s3.amazonaws.com/udacity-dsand/testdir.zip):

./testdir
./testdir/subdir1
./testdir/subdir1/a.c
./testdir/subdir1/a.h
./testdir/subdir2
./testdir/subdir2/.gitkeep
./testdir/subdir3
./testdir/subdir3/subsubdir1
./testdir/subdir3/subsubdir1/b.c
./testdir/subdir3/subsubdir1/b.h
./testdir/subdir4
./testdir/subdir4/.gitkeep
./testdir/subdir5
./testdir/subdir5/a.c
./testdir/subdir5/a.h
./testdir/t1.c
./testdir/t1.h

Python's os module will be useful—in particular, you may want to use the following resources:

os.path.isdir(path) (https://docs.python.org/3.7/library/os.path.html#os.path.isdir)

os.path.isfile(path) (https://docs.python.org/3.7/library/os.path.html#os.path.isfile)

os.listdir(directory) (https://docs.python.org/3.7/library/os.html#os.listdir)

os.path.join(...) (https://docs.python.org/3.7/library/os.path.html#os.path.join)

Note: os.walk() is a handy Python method which can achieve this task very easily. However, for this problem you are not allowed to use os.walk().

OS Module Exploration Code

## Locally save and call this file ex.py ##

# Code to demonstrate the use of some of the OS modules in python

import os

# Let us print the files in the directory in which you are running this script
print (os.listdir("."))

# Let us check if this file is indeed a file!
print (os.path.isfile("./ex.py"))

# Does the file end with .py?
print ("./ex.py".endswith(".py"))
"""

import os  # import os module


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
    if not suffix or not path:
        print("Inputs suffix and/or path cannot be None")
        return None
    if not os.path.exists(path):
        print("Path is not valid")
        return None

    files = []  # create empty list to store files
    if os.path.isfile(path):  # check if path is a file
        if path.endswith(suffix):  # check if file ends with suffix
            files.append(path)  # append file to list
    elif os.path.isdir(path):  # check if path is a directory
        for file in os.listdir(path):  # iterate through files in directory
            files += find_files(suffix, os.path.join(path, file))  # recursively call function

    return files  # return list of files


# Add your own test cases: include at least three test cases
# and two of them must include edge cases, such as null, empty or very large values

# Find cases of .c file extension
# Test Case 1
def test_01():
    files = find_files(".c", "./testdir")
    assert len(files) == 4, "Test Case 1 Failed"
    assert "./testdir/subdir1/a.c" in files, "Test Case 1 Failed"
    assert "./testdir/subdir3/subsubdir1/b.c" in files, "Test Case 1 Failed"
    assert "./testdir/t1.c" in files, "Test Case 1 Failed"
    assert "./testdir/subdir5/a.c" in files, "Test Case 1 Failed"
    print("Test Case 1 Passed")


test_01()

# Find cases of .c file extension in a subdirectory
# Test Case 2
def test_02():
    files = find_files(".c", "./testdir/subdir1")
    assert len(files) == 1, "Test Case 2 Failed"
    assert "./testdir/subdir1/a.c" in files, "Test Case 2 Failed"
    print("Test Case 2 Passed")


test_02()

# Testing case where None is passed as suffix
# Test Case 3
def test_03():
    files = find_files(None, "./testdir")
    assert files == None, "Test Case 3 Failed"
    print("Test Case 3 Passed")


test_03()


# Testing case where None is passed as path
# Test Case 4
def test_04():
    files = find_files(".c", None)
    assert files == None, "Test Case 4 Failed"
    print("Test Case 4 Passed")


test_04()


# Testing case where a non-existent path is passed
# Test Case 5
def test_05():
    files = find_files(".c", "./testdir/invalid")
    assert files == None, "Test Case 5 Failed"
    print("Test Case 5 Passed")


test_05()
