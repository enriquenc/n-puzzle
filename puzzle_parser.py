import fileinput
import re
from error import Error, error

#!TODO Возможность сохранения комментариев в файл по флагу.
#!TODO Добавить парсер флагов


class Parser:
    def __init__(self):
        self.size = 0
        self.puzzle_elements = []
        self.max_value = 0
        self.puzzle = []


    def find_size(self, line):
        line = self.clear_line(line)
        if line == "#":
            return
        elif re.match(r"^[0-9]*$", line) is not None:
            self.size = int(line)
        else:
            error(Error.ERROR_SIZE)

        if self.size < 3:
            error(Error.ERROR_MIN_SIZE)

        self.puzzle_elements = [[0] * (self.size * self.size)][0]
        self.max_value = self.size * self.size - 1

    @staticmethod
    def clear_line(line):
        line = line.rstrip(' \n')
        if line == "":
            error(Error.ERROR_EMPTY_LINE)
        line = line.split('#')
        if line[0] == "":
            return "#"
        return line[0].strip()

    def find_puzzle(self, line):

        line = self.clear_line(line)
        if line == "#":
            return False

        if re.match(r"^[0-9 ]*$", line) is None:
            error(Error.ERROR_ROW_ITEMS)

        line = line.split(' ')

        for l in line:
            if l == '':
                line.remove(l)

        if len(line) != self.size:
            error(Error.ERROR_ELEMENTS_AMOUNT, "Should be " + str(self.size) + " elements.")

        self.check_row(line)
        for i in range(len(line)):
            line[i] = int(line[i])
        self.puzzle.append(line)

        if len(self.puzzle) == self.size:
            return True

    def check_row(self, line):
        for elem in line:
            elem = int(elem)
            if elem > self.max_value:
                error(Error.ERROR_BIG_ELEMENT, " Max element - " + str(self.max_value) + '.')
            if self.puzzle_elements[elem] == 0:
                self.puzzle_elements[elem] = 1
            else:
                error(Error.ERROR_ELEMENT_EXISTS, str(elem) + '.')

    def get_input(self, file=None):
        if file is not None:
            with fileinput.input(file) as f:
                for line in f:
                    if self.size == 0:
                        self.find_size(line)
                    elif self.find_puzzle(line) is True:
                        break
        else:
            for line in fileinput.input():
                if self.size == 0:
                    self.find_size(line)
                elif self.find_puzzle(line) is True:
                    break
        fileinput.close()



if __name__ == "__main__":
    p = Parser()
    p.find_size()
    print(p.get_puzzle())






