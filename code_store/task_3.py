"""
Task 3
"""


import pathlib
import colorama


def get_files_and_folders(path: pathlib.Path, depth: int = 0) -> None:
    """
    Function to get files and folders in a path

    Args:
    path (str): The path to the folder
    depth (int): The depth of the folder

    Returns:
    None
    """
    tab = "  " * depth
    folder_to_skip = ['venv',
                      '.git', 
                      '.DS_Store', 
                      '.gitattributes', 
                      '__pycache__']

    for item in path.iterdir():
        if item.name in folder_to_skip:
            continue
        if item.is_dir():
            print(tab + colorama.Fore.BLUE + f'{item.name}')
            get_files_and_folders(item, depth + 1)
        else:
            print(tab + colorama.Fore.GREEN + f'{item.name}')
