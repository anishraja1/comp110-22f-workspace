"""Dictionary Functions (invert, count, favorite colors)."""
__author__: str = "730575619"


def invert(dictionary: dict[str, str]) -> dict[str, str]:
    """Inverts a dictionary."""
    if dictionary == {}:  # If an empty dictionary is given, it returns an empty dictionary.
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
    new_list: list[str] = []
    stored_num: int = 0
    for key in count:  # Iterates through and ensures that the color with the highest value is stored in new_list.
        if stored_num == 0:
            new_list.append(key)
            stored_num += count[key]
        else: 
            if count[key] > stored_num:
                new_list[0] = key
                stored_num = count[key]
    return new_list[0]  # Returns the color


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