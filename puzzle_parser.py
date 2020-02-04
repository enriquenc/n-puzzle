import fileinput
import re
from error import Error, error
from argparser import args
import sys

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
        if args.save is not None and len(line) > 1:
            f = open(args.save, 'a')
            f.write(line[1] + '\n')
            f.close()
        if line[0] == "":
            return "#"
        return line[0].strip()

    def find_puzzle(self, line):

        line = self.clear_line(line)
        if line == "#":
            # skip lines with comments
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

    @staticmethod
    def check_input_files():
        if args.filename is not None:
            try:
                open(args.filename, 'r').close()
            except:
                error(Error.ERROR_READ_FILE, '\'' + args.filename + '\'')
        if args.save is not None:
            try:
                open(args.save, 'a').close()
            except:
                error(Error.ERROR_SAVE_FILE, '\'' + args.save + '\'')

    def get_input(self, file=None):
        global args
        self.check_input_files()
        if args.filename is not None:
            file = args.filename
        if file is not None:
            with fileinput.input(file) as f:
                for line in f:
                    if self.size == 0:
                        self.find_size(line)
                    elif self.find_puzzle(line) is True:
                        break
        else:
            while True:
                line = input()
                if self.size == 0:
                    self.find_size(line)
                elif self.find_puzzle(line) is True:
                    break
        fileinput.close()







