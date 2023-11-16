from filesys.functions.devs_defaults_v1 import *

def delfile(data_file):
    """
        data_file: The path to the file you want to be deleted.
    """
    if ok.path.exists(data_file):
        ok.remove(data_file)
    else:
        print("no such file exists!")

def delfolder(data_folder):
    """
        data_folder: The path to the desired folder you want to be deleted.
    """
    if ok.path.exists(data_folder):
        ok.rmdir(data_folder)
    else:
        print("no such folder exists!")