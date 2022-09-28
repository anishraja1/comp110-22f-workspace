"""Contains unit test functions for ex05_utils"""
__author__ = "730575619"

from exercises.ex05.utils import only_evens
from exercises.ex05.utils import sub
from exercises.ex05.utils import concat

# For only_evens function. 
# This test checks to see if a list of odds returns an empty list. 
def test_only_evens_odds() -> None:
    """This test checks to see if a list of odds returns an empty list. """
    list_given: list[int] =  [1,5,3]
    assert only_evens(list_given) == []
# This test checks to see if an empty list returns an empty list. 
def test_only_evens_empty() -> None:
    """This test checks to see if a single odd list brings up an assertion error. """
    list_given: list[int] =  ['a']
    assert only_evens(list_given) == []
# Checks to see if a list with evens and odds only returns the evens.
def test_only_evens_both() -> None:
    """Checks to see if a list with evens and odds only returns the evens."""
    list_given: list[int] =  [2,1,4]
    assert only_evens(list_given) == [2,4]


# For concat function.
# Tests to see if two lists of different lengths will return a combined list.
def test_concat_one() -> None:
    """Tests to see if two lists of different lengths will return a combined list."""
    list_one: list[int] = [1,2,5,6]
    list_two: list[int] = [3,7,8,8]
    assert concat(list_one,list_two) == [1,2,5,6,3,7,8,8]
# This tests to see if two lists will return a combined list.
def test_concat_two() -> None:
    """Tests to see if two lists will return a combined list."""
    list_one: list[int] = [1,3,7,5]
    list_two: list[int] = [2]
    assert concat(list_one,list_two) == [1,3,7,5,2]
# Tests to see if an assertion error is brought by the incorrect assertion output.
def test_concat_three() -> None:
    """Tests to see if an assertion error is brought by the incorrect assertion output"""
    list_two: list[int] = [2]
    assert concat(list_one,list_two) == [3,3,3]


# For sub function
# Tests to see if output includes list from start to end index (non-included).
def test_sub_one() -> None:
    """Tests to see if output includes list from start to end index (non-included)."""
    list_one: list[int] = [10,15,20,25,30]
    assert sub(list_one,1,3)
# "Tests to see if output includes list from start to end index (non-included)
def test_sub_two() -> None:
    """Tests to see if output includes list from start to end index (non-included)"""
    list_one: list[int] = [1,2,3,4,5,6,7,8,9]
    assert sub(list_one,3,6)
# Tests to see if there is assertion error since index of 6 is out of range.
def test_sub_three() -> None:
    """Tests to see if there is assertion error since index of 6 is out of range."""
    list_one: list[int] = [2,4,6,8,10]
    assert sub(list_one,1,6)