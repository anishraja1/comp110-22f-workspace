"""Dictionary related utility functions."""
__author__ = "730575619"


from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read the rows of a csv into a table."""
    result: list[dict[str, str]] = []  # List that will be returned
    # Open a handle to the data file
    file_handle = open(filename, "r", encoding="utf8")  # Opens the file in read mode
    # Prepare to read the data file as a CSV rather than just strings
    csv_reader = DictReader(file_handle)  # CSV Readers / Decipherer
    # Read each row of the CSV line-by-line
    for row in csv_reader:  # Deciphers and adds values to list
        result.append(row)
    # Close the file when we're done to free its resources
    file_handle.close()
    return result


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Produce a list[str] of all values in a single column."""
    result: list[str] = []  # List that will be returned
    for row in table:  # Loops through each row, the grabs a value from the specified column
        item: str = row[column]
        result.append(item)
    return result


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a row-oriented table to a column-oriented table."""
    result: dict[str, list[str]] = {}  # List to be returned
    first_row: dict[str, str] = row_table[0]  # Looks at first item
    for column in first_row:
        result[column] = column_values(row_table, column)
    return result


def head(column_table: dict[str, list[str]], num_of_rows: int) -> dict[str, list[str]]:
    """Produce a column-based table with only the first "x" rows of data for each column."""
    result: dict[str, list[str]] = {}  # List to be returned
    for column in column_table:
        number_of_rows: int = num_of_rows
        if number_of_rows >= len(column_table[column]):
            number_of_rows = len(column_table[column])
        stored_values: list[str] = []
        for num in range(0, number_of_rows):  # Appends the desired number of values 
            stored_values.append(column_table[column][num])
        result[column] = stored_values
    return result


def select(column_table: dict[str, list[str]], column_names: list[str]) -> dict[str, list[str]]:
    """Produce a new column-based table with only a specific sibset of the original columns."""
    result: dict[str, list[str]] = {}  # List to be returned
    for column in column_table:
        if column in column_names:  # Checks if column is in table
            result[column] = column_table[column]
    return result


def concat(column_table_one: dict[str, list[str]], column_table_two: dict[str, list[str]]) -> dict[str, list[str]]:
    """Produce a new column-based table witht wo column-based tables combined."""
    result: dict[str, list[str]] = {}  # List to be returened
    for column in column_table_one:  # Adds key and values
        result[column] = column_table_one[column]
    for column in column_table_two:
        if column in result:  # If key exists, it adds on to the values
            result[column] += column_table_two[column]
        else:
            result[column] = column_table_two[column]  # Else, it creates a new key and value
    return result


def count(input_list=list[str]) -> dict[str, int]:
    """Will produce a dict[str, int] where each key is a unique value in the given list and each value associated is the count of the number of times that value appeared in the input list."""
    result: dict[str, int] = {}  # List to be returned
    for item in input_list:  # If item doesn't exist, it adds a key and sets the value to one. If it does, then it increments the value of that key by one.
        if item in result:
            result[item] += 1
        else:
            result[item] = 1
    return result