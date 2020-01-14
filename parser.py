import fileinput
import re
import enum

#!TODO Возможность сохранения комментариев в файл по флагу.

class Error(enum.Enum):
    ALL_OK = 0
    ERROR_SIZE = "Invalid puzzle size. "
    ERROR_ROW_ITEMS = "Invalid puzzle row items. "
    ERROR_ELEMENTS_AMOUNT = "Invalid amount of elements in the row. "
    ERROR_BIG_ELEMENT = "Very big element of puzzle. "
    ERROR_ELEMENT_EXISTS = "Multiple input of puzzle element: "
    ERROR_EMPTY_LINE = "Empty lines doesn't accept."


class Parser:
    def __init__(self, color=0):
        self.size = 0
        self.color = color
        self.puzzle_elements = []
        self.max_value = 0

    def find_size(self):
        for line in fileinput.input():
            line = self.clear_line(line)
            if line == "#":
                continue
            elif re.match(r"^[0-9]*$", line) is not None:
                self.size = int(line)
            else:
                self.error(Error.ERROR_SIZE)

            self.puzzle_elements = [[0] * (self.size * self.size)][0]
            self.max_value = self.size * self.size - 1

            fileinput.close()
            return

    def clear_line(self, line):
        line = line.rstrip(' \n')
        if line == "":
            self.error(Error.ERROR_EMPTY_LINE)
        line = line.split('#')
        if line[0] == "" and line[1] != "":
            return "#"
        return line[0].strip()

    def get_puzzle(self):
        puzzle = []
        for line in fileinput.input():
            line = self.clear_line(line)
            if line == "#":
                continue

            if re.match(r"^[0-9 ]*$", line) is None:
                self.error(Error.ERROR_PUZZLE_ROW)

            line = line.split(' ')

            if len(line) != self.size:
                self.error(Error.ERROR_ELEMENTS_AMOUNT, "Should be " + str(self.size) + " elements.")

            self.check_row(line)
            puzzle.append(line)

            if len(puzzle) == self.size:
                fileinput.close()
                return puzzle

    def check_row(self, line):
        for elem in line:
            elem = int(elem)
            if elem > self.max_value:
                self.error(Error.ERROR_BIG_ELEMENT, " Max element - " + str(self.max_value) + '.')
            if self.puzzle_elements[elem] == 0:
                self.puzzle_elements[elem] = 1
            else:
                self.error(Error.ERROR_ELEMENT_EXISTS, str(elem) + '.')

    def error(self, err, data=''):
        s = ""
        if self.color:
            s += '\x1b[1;31m'

        s += "ERROR. " + err.value + data

        if self.color:
             s += '\x1b[0m'
        print(s)
        exit(0)



p = Parser(1)
p.find_size()
print(p.get_puzzle())






