"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = "730575619"


class Simpy:
    """Simpy class that makes it easy to work with sequences of numerical data."""
    values: list[float]

    def __init__(self, list_one: list[float]):
        """Assigns list_one to self.values."""
        self.values = list_one
    
    def __repr__(self) -> str:
        """Prints self.values in a string format."""
        return f"Simpy({self.values})"

    def fill(self, float_num: float, int_num: int) -> None:
        """Fill a Simpy's values with a specific number of repeating values."""
        self.values = []
        for i in range(int_num):
            self.values.append(float_num)
        
    def arange(self, start: float, stop: float, step: float = 1.0) -> None:
        """Fills in the values attribute with a range of values in term of floats."""
        assert step != 0.0
        while start != stop:
            self.values.append(start)
            start += step

    def sum(self) -> float:
        """Compute and return the sum of all items in the values attribute."""
        return sum(self.values)

    def __add__(self, rhs: Union[Simpy, float]) -> Simpy:
        """Addition operator that adds two Simpy objects or one Simpy object with the given float."""
        if isinstance(rhs, Simpy):
            assert len(self.values) == len(rhs.values)
            new_list: list[float] = []
            for i in range(len(self.values)):
                new_list.append(self.values[i] + rhs.values[i])
            new_object: Simpy = Simpy(new_list)
            return new_object
        elif isinstance(rhs, float):
            new_list: list[float] = []
            for i in range(len(self.values)):
                new_list.append(self.values[i] + rhs)
            new_object: Simpy = Simpy(new_list)
            return new_object

    def __pow__(self, rhs: Union[Simpy, float]) -> Simpy:
        """Raises the value of items in a list by the respective value in rhs or by a constant float value."""
        if isinstance(rhs, Simpy):
            assert len(self.values) == len(rhs.values)
            new_list: list[float] = []
            for i in range(len(self.values)):
                new_list.append(self.values[i] ** rhs.values[i])
            new_object: Simpy = Simpy(new_list)
            return new_object
        elif isinstance(rhs, float):
            new_list: list[float] = []
            for i in range(len(self.values)):
                new_list.append(self.values[i] ** rhs)
            new_object: Simpy = Simpy(new_list)
            return new_object

    def __eq__(self, rhs: Union[Simpy, float]) -> list[bool]:
        """Checks if each item in a list is equal to an item in another list. Returns a mask."""
        if isinstance(rhs, Simpy):
            assert len(self.values) == len(rhs.values)
            list_of_bool: list[bool] = []
            for i in range(len(self.values)):
                list_of_bool.append(self.values[i] == rhs.values[i])
            return list_of_bool
        elif isinstance(rhs, float):
            list_of_bool: list[bool] = []
            for i in range(len(self.values)):
                list_of_bool.append(self.values[i] == rhs)
            return list_of_bool

    def __gt__(self, rhs: Union[Simpy, float]) -> list[bool]:
        """Checks if each item in a list is greater than an item in another list. Returns a mask."""
        if isinstance(rhs, Simpy):
            assert len(self.values) == len(rhs.values)
            list_of_bool: list[bool] = []
            for i in range(len(self.values)):
                list_of_bool.append(self.values[i] > rhs.values[i])
            return list_of_bool
        elif isinstance(rhs, float):
            list_of_bool: list[bool] = []
            for i in range(len(self.values)):
                list_of_bool.append(self.values[i] > rhs)
            return list_of_bool

    def __getitem__(self, rhs: Union[int, list[bool]]) -> Union[float, Simpy]:
        """Allows for subscription notation support to objects of classes."""
        if isinstance(rhs, int):
            return self.values[rhs]
        else:
            new_list: list[float] = []
            for i in range(len(self.values)):
                if rhs[i]:
                    new_list.append(self.values[i])
            new_object: Simpy = Simpy(new_list)
            return new_object
    
            




   
