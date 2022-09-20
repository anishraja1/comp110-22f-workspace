"""Example implementing a list utility function."""
__author__ = "730575619"


# Function name: contains
# We will have two parameters: needle (str), haystack (list[str]
# Return type: bool

def contains(needle: str, haystack: list[str]) -> bool:
# Gameplan:
# 1) Start with the first index
    i: int = 0
# 2) Loop through every index
    while i < len(haystack):
#   2.A) Test if item at index is equal to needle
        if haystack[i] == needle:
#       2.A.True) Return True! We found it!
            return True
        i += 1
#   2.B) Return False
    return False
