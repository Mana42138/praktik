from filesys.functions.devs_defaults_v1 import *

def isfile(data_file):
    if ok.path.isfile(data_file):
        return True
    else:
        return False

def isfolder(folder_path):
    if ok.path.exists(folder_path):
        return True
    else:
        return False