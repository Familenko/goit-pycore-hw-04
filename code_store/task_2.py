"""
Task 2
"""


from typing import Dict


def get_cats_info(path: str) -> list[Dict]:
    """
    Function to get cats info from a file

    Args:
    path (str): The path to the file

    Returns:
    list[Dict]: A list of dictionaries with cats info
    """
    try:
        with open(path, 'r', encoding='utf-8') as f:
            data = f.readlines()
    except (FileNotFoundError, IOError):
        return print('File not found or have error')

    data = [line.strip() for line in data]

    cats = []

    for line in data:
        if not line:
            continue

        cat = {}
        if len(line.split(',')) != 3:
            return print('Error in data')
        cat['id'], cat['name'], cat['age'] = line.split(',')
        cats.append(cat)

    return cats
