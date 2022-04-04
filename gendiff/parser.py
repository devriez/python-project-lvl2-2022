import os
import yaml


def file_parsing(path):
    """
    Read files with a given file names and return list of files structure.
    Parameters:
        file_path: The path to the file to read.
    Returns:
        File content, parsed to the dictionary.
    """
    absolute_path = os.path.abspath(path)
    data = yaml.safe_load(open(absolute_path))
    return data
