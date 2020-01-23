from copy import deepcopy, Error
import hashlib
import math


current_number_of_nodes = 0


class Board:
    def __init__(self, parent=None, move=0):
        self.puzzle = None
        self.hash = None
        self.g = 0
        self.size = 0
        self.zero_index = 0
        self.h = 0
        self.f = 0
        if parent:
            self.g = parent.g + 1
            self.puzzle = self.set_puzzle(parent.puzzle, move)
        self.parent = parent
        global current_number_of_nodes
        current_number_of_nodes += 1

    def __del__(self):
        global current_number_of_nodes
        current_number_of_nodes -= 1

    def set_puzzle(self, puzzle, move=0):
        self.puzzle = puzzle.copy()
        self.size = int(math.sqrt(len(self.puzzle)))
        self.hash = self.hash_puzzle(self.puzzle)
        self.zero_index = self.puzzle.index(0)
        self.calculate_puzzle(move)
        self.hash = self.hash_puzzle(self.puzzle)
        return self.puzzle

    def calculate_puzzle(self, move):
        temp = self.puzzle[self.zero_index + move]
        self.puzzle[self.zero_index] = temp
        self.puzzle[self.zero_index + move] = 0
        self.zero_index = self.zero_index + move

    def neighbors(self):
        res = []

        if self.zero_index % self.size != 0:
            res.append(Board(self, -1))
        if self.zero_index % self.size < (self.size - 1):
            res.append(Board(self, 1))
        if self.zero_index - self.size >= 0:
            res.append(Board(self, -self.size))
        if self.zero_index + self.size < self.size * self.size:
            res.append(Board(self, self.size))
        return res

    @staticmethod
    def hash_puzzle(puzzle):
        s = 1
        for el in puzzle:
                s *= 10
                s += el
        return s


class Algorithm:
    def __init__(self, puzzle, size):
        self.puzzle_end_state = self.puzzle_to_row(self.get_end_puzzle_state(size))
        self.end_hash = Board.hash_puzzle(self.puzzle_end_state)

        self.puzzle = self.puzzle_to_row(puzzle)
        self.size = size
        self.close = []
        self.open = []

        self.total_opened_nodes = 0
        self.max_number_in_memory = 0
        self.solve_steps_amount = 0


    def pop_open(self):
        min = self.open[0]
        for i in self.open:
            if min.f > i.f:
                min = i
        return self.open.pop(self.open.index(min))

    def empty_open(self):
        return self.open == []

    def push_open(self, elem):
        self.open.append(elem)
        self.total_opened_nodes += 1
        return

    @staticmethod
    def get_end_puzzle_state(size):
        puzzle = [[0 for x in range(size)] for y in range(size)]
        num = 1
        end = size * size - 1
        i = 0
        j = 0
        k = 1
        level = 0
        num_to_next_level = 0
        while num <= end:
            puzzle[i][j] = num
            num += 1
            if num_to_next_level + (size - k) * 4 == num:
                num_to_next_level += (size - k) * 4
                level += 1
                k += 2
            if j == size - level - 1 and i < size - level - 1:
                i += 1
            elif i == size - level - 1 and j > level:
                j -= 1
            elif i > level:
                i -= 1
            elif j < size - level - 1:
                j += 1

        return puzzle

    def is_already_solved(self):
        return Board.hash_puzzle(self.puzzle) == Board.hash_puzzle(self.puzzle_end_state)

    @staticmethod
    def puzzle_to_row(puzzle):
        puzzle_row = []
        for line in puzzle:
            for elem in line:
                #if elem:
                puzzle_row.append(elem)
        return puzzle_row

    def is_solvable(self):
        count_inversions = 0

        for i in range(len(self.puzzle)):
            for j in range(i):
                if self.puzzle[j] > self.puzzle[i]:
                    count_inversions += 1

        return count_inversions % 2 != 0


    def solve(self):

        #self.puzzle = [item for sublist in self.puzzle for item in sublist]
        start = Board()
        start.set_puzzle(self.puzzle)
        start.f = self.heuristic(start.puzzle)
        self.push_open(start)
        current = None

        while self.empty_open() is False:
            #print(len(self.open))
            #print(self.pop_open())
            #print(self.close)
            current = self.pop_open()
            #if current.hash in self.close:
            #    continue

            self.close.append(current.hash)
            if current.hash == self.end_hash:
                self.solve_steps_amount = current.g
                return current


            # for n in current.neighbors():
            #     if n.hash in self.close:
            #         continue
            #     n.h = self.heuristic(n.puzzle)
            #
            #     if n.h <= self.min_open():
            #          self.push_open(n)
            for n in current.neighbors():
                if n.hash in self.close:
                    continue
                n.f = current.g + self.heuristic(n.puzzle)
                if n not in self.open:
                    self.push_open(n)
                #else:
                #    self.open[self.open.index(n)].f = current.g + self.heuristic(n.puzzle)

            if current_number_of_nodes > self.max_number_in_memory:
                self.max_number_in_memory = current_number_of_nodes
                #print(self.max_number_in_memory)

        return current

    def find_elem_cord(self, el):
        for i in range(len(self.puzzle_end_state)):
            if self.puzzle_end_state[i] == el:
                return i

    def heuristic(self, puzzle):
        h = 0
        for i in range(len(puzzle)):
                end_element_index = self.find_elem_cord(puzzle[i])
                div = abs(i - end_element_index)
                if div % self.size == 0:
                    h += div // self.size
                else:
                    h += (self.size - div % self.size) + (div + self.size) // self.size
        return h

if __name__ == "__main__":
    a = Algorithm(3)
    for i in a.puzzle_end_state:
        print(i)