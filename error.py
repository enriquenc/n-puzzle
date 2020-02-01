import enum


class Error(enum.Enum):
    ERROR_SIZE = "Invalid puzzle size. "
    ERROR_MIN_SIZE = "Invalid puzzle size. Min size - 3."
    ERROR_ROW_ITEMS = "Invalid puzzle row items. "
    ERROR_ELEMENTS_AMOUNT = "Invalid amount of elements in the row. "
    ERROR_BIG_ELEMENT = "Very big element of puzzle. "
    ERROR_ELEMENT_EXISTS = "Multiple input of puzzle element: "
    ERROR_EMPTY_LINE = "Empty lines doesn't accept."
    ERROR_FILE = "Error file entered."


class Success(enum.Enum):
    ALREADY_SOLVED = "You entered solved puzzle."


def error(err, data=''):
    s = "\n"
    color = 1
    if color:
        s += '\x1b[1;31m'
    s += "ERROR. " + err.value + data
    if color:
         s += '\x1b[0m'
    print(s)
    exit(0)


def success(err):
    print("\033[92m\n{}\033[00m".format(err.value))
    exit(0)
