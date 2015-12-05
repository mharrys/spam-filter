"""File system wrapper.
"""
import os


def read_file(path):
    """Return decoded file content for specified path
    """
    fptr = open(path, 'r')
    content = fptr.read()
    fptr.close()
    return content.decode('latin1')


def dir_contents(path, sort=True):
    """Return list of all entries in a directory for specified path.
    """
    contents = [os.path.join(path, f) for f in os.listdir(path)]
    return sorted(contents) if sort else contents


def dir_walk(path, sort=True):
    """Return list of all entries in a directory tree for specified path.
    """
    contents = []
    for root, _, files in os.walk(path):
        contents += [os.path.join(root, f) for f in files]
    return sorted(contents) if sort else contents
