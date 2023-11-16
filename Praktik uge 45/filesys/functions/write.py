from filesys.functions.devs_defaults_v1 import *

def writefile(data_file, data):
    """
    data_file: The path location you want the file to be written.
    data: The data you want to be inserted into the file.
    """
    full_path = ok.path.abspath(data_file)
    directory = ok.path.dirname(full_path)

    ok.makedirs(directory, exist_ok=True)

    with open(full_path, "w") as f:
        jn.dump(data, f, indent=4)


def makefolder(folder_path):
    """
    folder_path: The path you want to place the desired folder.
    """
    full_path = ok.path.abspath(folder_path)

    ok.makedirs(full_path, exist_ok=True)
    