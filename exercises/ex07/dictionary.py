"""Dictionary Functions (invert, count, favorite colors)."""
__author__: str = "730575619"


import pytest


def invert(dictionary: dict[str, str]) -> dict[str, str]:
    """Inverts a dictionary."""
    if dictionary =={}:  # If an empty dictionary is given, it returns an empty dictionary.
        return {}
    result: dict[str, str] = {}
    for key in dictionary:  # Iterates through dictionary to assigns the values as the key to the results dictionary.
        if dictionary[key] in result:
            raise KeyError("KeyError. Dictionary has multiple keys with the same value.")  # Raises a keyerror if multiple similar values exist
        else:
         result[dictionary[key]] = key
    return result


def favorite_color(dictionary: dict[str, str]) -> str:
    """Returns the most common value in a dictionary."""
    if dictionary == {}:  # If an empty dictionary is given, it returns an empty dictionary.
        return {}
    count: dict[str, int] = {}
    for key in dictionary:  # Iterates through dictionary to invert it and finds the greatest occurence and returns that string.
        if dictionary[key] in count:
            count[dictionary[key]] += 1
        else:
            count[dictionary[key]] = 1
    result_two: dict[str, str] = {}
    for key in count:
        result_two[count[key]] = key
    greatest_number: int = 0  # Stores the number value  of greatest occurence
    for key in result_two:
        if key > greatest_number:
            greatest_number = key
    return result_two[greatest_number]  # Returns the color



def count(list_one: list[str]) -> dict[str, int]:
    """Creates a dictionary with al values and the numbe of occurences."""
    if list_one == []:  # If given an empty list, it ®eturns an empty dictionary.
        return {}
    count_two: dict[str, int] = {}
    for item in list_one:  # Iterates through list and creates a dictionary.
        if item in count_two:
            count_two[item] += 1
        else:
            count_two[item] = 1
    return count_two






