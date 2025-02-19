"""Examples of importing Python."""


from lessons import helpers  # from a package import a module

# Alias a module / imported name as another name
from lessons import helpers as hp

# import names defined globally in a module
from lessons.helpers import powerful, THE_ANSWER

def main() -> None:
    """Entrypoing of program."""
    print(helpers.powerful(2,4))
    print(f"The answer: {hp.THE_ANSWER}")
    print(powerful(2,4))
    print(THE_ANSWER)

if __name__ == "__main__":
    main()