from copy import deepcopy, Error
import hashlib
import math
from argparser import args
from priority_queue import myPriorityQueue
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

    def calculate_f(self):
        self.f = self.h + self.g

    def __lt__(self, other):
        return self.f < other.f

    def __del__(self):
        global current_number_of_nodes
        current_number_of_nodes -= 1

    def set_puzzle(self, puzzle, move=0):
        self.puzzle = puzzle.copy()
        self.size = int(math.sqrt(len(self.puzzle)))
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
        self.open = myPriorityQueue()

        self.total_opened_nodes = 0
        self.max_number_in_memory = 0
        self.solve_steps_amount = 0

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

    def is_solvable(puzzle):
        list_puzzle = []
        size = len(puzzle)
        num = 1
        end = size * size - 1
        i = 0
        j = 0
        k = 1
        level = 0
        num_to_next_level = 0
        while num <= end:
            list_puzzle.append(puzzle[i][j])
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
        list_puzzle.append(puzzle[size // 2][(size - 1) // 2])
        count_inversions = list_puzzle.index(0)
        for i in range(len(list_puzzle)):
            for j in range(i + 1, len(list_puzzle)):
                if list_puzzle[j] < list_puzzle[i]:
                    count_inversions += 1
        return count_inversions % 2 == 0


    def solve(self):
        start = Board()
        start.set_puzzle(self.puzzle)
        start.f = self.heuristic(start.puzzle)
        self.open.push(start)
        self.total_opened_nodes += 1
        current = None

        while self.open.isEmpty() is False:

            current = self.open.pop()

            self.close.append(current.hash)
            if current.hash == self.end_hash:
                self.solve_steps_amount = current.g
                return current

            for n in current.neighbors():
                if n.hash in self.close:
                    continue
                n.h = self.heuristic(n.puzzle)
                n.calculate_f()
                self.open.push(n)
                self.total_opened_nodes += 1


            if current_number_of_nodes > self.max_number_in_memory:
                self.max_number_in_memory = current_number_of_nodes

        return current

    def heuristic(self, puzzle):
        if args.heuristic == 2:
            return self.heuristic_chiponpos(puzzle)
        elif args.heuristic == 3:
            return self.heuristic_euclidist(puzzle)
        else:
            return self.heuristic_manhattan(puzzle)

    def heuristic_chiponpos(self, puzzle):
        h = 0
        for el in self.puzzle:
            if self.puzzle.index(el) != self.puzzle_end_state.index(el):
                h += 1
        return h * args.increase

    def heuristic_euclidist(self, puzzle):
        h = 0
        for i in range(len(puzzle)):
                end_element_index = self.puzzle_end_state.index(puzzle[i])
                start_element_i = i // self.size
                start_element_j = i % self.size
                end_element_j = end_element_index % self.size
                end_element_index = end_element_index // self.size
                h += math.sqrt(abs(start_element_i - end_element_index)**2 + abs(start_element_j - end_element_j)**2)
        return h * args.increase

    def heuristic_manhattan(self, puzzle):
        h = 0
        for i in range(len(puzzle)):
                end_element_index = self.puzzle_end_state.index(puzzle[i])
                start_element_i = i // self.size
                start_element_j = i % self.size
                end_element_j = end_element_index % self.size
                end_element_index = end_element_index // self.size
                h += abs(start_element_i - end_element_index) + abs(start_element_j - end_element_j)
        return h * args.increase