"""Contains test functions for the dictionary functions."""
__author__: str = "730575619"


from exercises.ex07.dictionary import invert
from exercises.ex07.dictionary import favorite_color
from exercises.ex07.dictionary import count
import pytest


def test_invert_one() -> None:
    """Tests if a key error will return."""
    this_dictionary: dict[str, str] = {'apple': 'fruit', 'banana': 'fruit'}  # dictionary input
    assert invert(this_dictionary) == {'fruit': 'apple', 'fruit': 'banana'}


def test_invert_two() -> None:
    """Test that gives an input with two different values and keys."""
    this_dictionary_two: dict[str, str] = {'apple': 'fruit', 'blue': 'color'}  # dictionary input
    assert invert(this_dictionary_two) == {'fruit': 'apple', 'color': 'blue'}


def test_invert_three() -> None:
    """Test with empty dictionary input."""
    this_dictionary_three: dict[str, str] = {}  # empty dictionary input
    assert invert(this_dictionary_three) == {}


def test_favorite_color() -> None:
    """Test with empty dictionary input."""
    dict_of_colors: dict[str, str] = {}  # empty dictionary input
    assert favorite_color(dict_of_colors) == {}


def test_favorite_color_two() -> None:
    """Test to see if most occurring color that comes first is returned."""
    dict_of_colors_two: dict[str, str] = {"Marc": "yellow", "Ezri": "blue", "Kris": "blue", 'Lisa': 'yellow', 'Roy': 'green'}  # dictionary input
    assert favorite_color(dict_of_colors_two) == "blue"


def test_favorite_color_three() -> None:
    """Test to see if most occuring color that is last is returned."""
    dict_of_colors_three: dict[str, str] = {"Marc": "yellow", "Ezri": "blue", "Kris": "green"}  # dictionary input
    assert favorite_color(dict_of_colors_three) == "green"


def test_count() -> None:
    """Test with input of multiple repeated values."""
    list_to_use: list[str] = ["apple", "orange", "banana", "banana", "apple"]  # list input
    assert count(list_to_use) == {"apple": 2, "orange": 1, "banana": 2}


def test_count_two() -> None:
    """Test with empty list input."""
    list_to_use_two: list[str] = []  # empty list input
    assert count(list_to_use_two) == {}


def test_count_three() -> None:
    """Test with input of multiple repeated values."""
    list_to_use_three: list[str] = ["apple", "banana", "banana", "banana", "apple"]  # list input
    assert count(list_to_use_three) == {"apple": 2, "banana": 3}
