#"""Will do later."""
__author__ = "730575619"

# Name: only_evens
# Arguments: A list of integer
# Returns: A list of integers, containing only the even elemenets of the input parameter
def only_evens(list_given: list[int]) -> list[int]:
    """Returns the given list with only even numbers if any."""
    list_returned: list[int] = []
    for item in list_given:
        if item % 2 == 0:
            list_returned.append(item)
    return list_returned


# Name: concat
# Parameters: Two lists of ints
# Returns: A list containing all elements of the first list, followed by all elements of the second list
def concat(list_one: list[int],list_two: list[int]) ->list[int]:
    """Concatenates two of the given lists together."""
    list_three: list[int] = []
    for i in list_one:
        list_three.append(i)
    for i in list_two:
        list_three.append(i)
    return list_three


# Name: sub
# Parameters: A list and two ints, where the first int serves as a start index and the second int serves as an end index (not inclusive)
# Returns: A list which is a subset of the given list, between the specified start index and the end index - 1
def sub(list: list[int], start_index: int, end_index: int) -> list[int]:
    """Returns a list between given start (inclusive) and end index"""
    returned_list: list[int] = []
    current_index: int = start_index
    while current_index != end_index:
        returned_list.append(list[current_index])
        current_index += 1
    return returned_list