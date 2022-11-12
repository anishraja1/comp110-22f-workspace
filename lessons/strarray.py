"""An example of vectorized operations via operator overloading."""

from __future__ import annotations
from typing import Union


class StrArray:
    items: list[str]

    def __init__(self, items: list[str]):
        self.items = items

    def __repr__(self) -> str:
        return f"StrArray({self.items})"

    def __add__(self, rhs: Union[str, StrArray]) -> StrArray:
        result: StrArray = StrArray([])
        if isinstance(rhs, str):
            for name in self.items:
                result.items.append(name + rhs)
            #   1. Loop through each item in self's item list
            #   2. Concatenate the rhs to the item value
            #   3. Append the resulting string to result's item's list
        else:
            assert len(self.items) == len(rhs.items)
            for i in range(len(self.items)):
                result.items.append(self.items[i] + rhs.items[i])
            return result
            #   1. Loop through each INDEX(!!!) of self's items list
            #   2. Concatenate the item at this index of self witht he corresponding time
            #   at the same index of the rhs's items list
            #   3. Append the concatenated string to resut's items list

        return result


a: StrArray = StrArray(["Armando", "Pete", "Leaky"])
b: StrArray = StrArray(["Bacot", "Mance", "Black"])
print(a)
print(a + "!")
print(a + b)
print(b + ", " + a + "!!!")