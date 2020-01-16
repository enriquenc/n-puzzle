import enum


class Error(enum.Enum):
    ALL_OK = 0
    ERROR_SIZE = "Invalid puzzle size. "
    ERROR_MIN_SIZE = "Invalid puzzle size. Min size - 3."
    ERROR_ROW_ITEMS = "Invalid puzzle row items. "
    ERROR_ELEMENTS_AMOUNT = "Invalid amount of elements in the row. "
    ERROR_BIG_ELEMENT = "Very big element of puzzle. "
    ERROR_ELEMENT_EXISTS = "Multiple input of puzzle element: "
    ERROR_EMPTY_LINE = "Empty lines doesn't accept."


def error(err, data=''):
    s = ""
    color = 1
    if color:
        s += '\x1b[1;31m'
    s += "ERROR. " + err.value + data
    if color:
         s += '\x1b[0m'
    print(s)
    exit(0)