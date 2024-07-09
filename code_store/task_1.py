"""
Task 1
"""


import re
from typing import Tuple


def total_salary(path: str) -> Tuple[int]:
    """
    Function to calculate total salary and mean salary from a file

    Args:
    path (str): The path to the file

    Returns:
    Tuple[int]: A tuple of total salary and mean salary
    """
    try:
        with open(path, 'r', encoding='utf-8') as f:
            data = f.read()
    except (FileNotFoundError, IOError):
        return print('File not found or have error')

    pattern = re.compile(r'\w+ \w+\,(\d+)')
    matches = pattern.findall(data)

    try:
        matches = [int(match) for match in matches]
    except ValueError:
        return print('Error in data')

    total = sum(matches)
    mean = total / len(matches) if total > 0 else 0

    return total, int(mean)
