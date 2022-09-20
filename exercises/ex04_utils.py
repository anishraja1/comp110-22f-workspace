"""List Utility Functions."""
__author__ = "730575619"


def all(x: list[int], y: int) -> bool:  # function that has two parameters: a list and int
    """Tests if the list is only made up of the integer."""
    i: int = 0  # initialized to zero
    length: int = len(x)  # length of the list
    while i < length:
        if x[i] != y:  # tests to see if list at the given index is equal the integer
            return False  # returns false if one match is wrong
        else: 
            i = i + 1
    return True  # returns true if all numbers match


def max(input: list[int]) -> int:
    """Finds the max value and also raises a ValueError if the list is empty."""
    if len(input) == 0:  # checks to see if list is empty
        raise ValueError("max() arg is an empty list")
    while len(input) != 1:  # makes sure all values are checked; only one list item left
        if input[0] > input[1]:  # this entire if-else sequence makes sure the bigger value stays and the lower value is popped out of the list
            input.pop(1)
        else:
            input.pop(0)
    return input[0]  # returns the remaining value (which is the max)


def is_equal(x: list[int], y: list[int]) -> bool:
    """Checks to see if the lists are identical to each other."""
    length_one: int = len(x)  # length of list one
    length_two: int = len(y)  # length of list two
    if length_one == length_two:  # checks to see if they are both the same length, and if they aren't, it returns False
        i: int = 0
        while i < length_one:  
            if x[i] == y[i]:  # checks to see if all the indexes are equal, and if they are, it will go to the return True at the very end
                i += 1
            else:  # if any list values don't match, it will return False
                return False
    else:
        return False
    return True

