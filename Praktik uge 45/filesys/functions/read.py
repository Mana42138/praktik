from filesys.functions.devs_defaults_v1 import *

def readfile(data_file : str):
    """
    data_file: The file path you want to read.
    """
    with open(data_file, "r") as f:
        data = jn.load(f)
    return data