from copy import deepcopy
import hashlib


class Board:
    def __init__(self, parent=None, i=0, j=0):
        self.puzzle = None
        self.hash = None
        self.g = 0
        self.size = 0
        self.zero_i = 0
        self.zero_j = 0
        self.h = 0
        if parent:
            self.g = parent.g + 1
            self.puzzle = self.set_puzzle(parent.puzzle, i, j)


        self.f = self.g + self.h
        self.parent = parent

    def set_puzzle(self, puzzle, i_=0, j_=0):
        self.puzzle = deepcopy(puzzle)
        self.size = len(puzzle)
        self.hash = self.hash_puzzle(self.puzzle)
        self.calculate_puzzle(i_, j_)
        for i in range(self.size):
            for j in range(self.size):
                if self.puzzle[i][j] == 0:
                    self.zero_i = i
                    self.zero_j = j
        self.hash = self.hash_puzzle(self.puzzle)
        return self.puzzle

    def calculate_puzzle(self, diff_i, diff_j):
        for i in range(len(self.puzzle)):
            for j in range(len(self.puzzle)):
                if self.puzzle[i][j] == 0:
                    # print(' ')
                    # print(diff_j)
                    # print(diff_i)
                    self.puzzle[i][j] = self.puzzle[i + diff_i][j + diff_j]
                    self.puzzle[i + diff_i][j + diff_j] = 0

                    return

    def neighbors(self):
        res = []


        #try:
        if self.zero_i - 1 >= 0:
            res.append(Board(self, -1, 0))
        if self.zero_j - 1 >= 0:
            res.append(Board(self, 0, -1))
        if self.zero_i + 1 < self.size:
            res.append(Board(self, 1, 0))
        if self.zero_j + 1 < self.size:
            res.append(Board(self, 0, 1))
        # except Exception as e:
        #     print(e)
        #     print(self.zero_i)
        #     print(self.zero_j)
        #     for i in self.puzzle:
        #         print(i)
        #     exit(0)
        # for i in res:
        #     for line in i.puzzle:
        #         print(line)
        #     print(' ')
        return res


    @staticmethod
    def hash_puzzle(puzzle):
        s = ""
        for i in puzzle:
            for j in i:
                s += str(j)
        return hashlib.sha256(s.encode('utf-8')).hexdigest()



class Algorithm:
    def __init__(self, puzzle, size):
        self.puzzle_end_state = self.get_end_puzzle_state(size)
        self.end_hash = Board.hash_puzzle(self.puzzle_end_state)
        self.puzzle = puzzle
        self.size = size
        self.close = []
        self.open = []

    def min_open(self):
        if self.open == []:
            return 0xFFFFFFFFFF
        else:
            return self.open[len(self.open) - 1].h

    def pop_open(self):
        return self.open.pop()

    def empty_open(self):
        return self.open == []

    def push_open(self, elem):
        self.open.append(elem)
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
        for i in range(self.size):
            for j in range(self.size):
                if self.puzzle_end_state[i][j] != self.puzzle[i][j]:
                    return False
        return True

    def is_solvable(self):
        count_inversions = 0
        puzzle_row = []
        for line in self.puzzle:
            for elem in line:
                if elem:
                    puzzle_row.append(elem)

        for i in range(len(puzzle_row)):
            for j in range(i):
                if puzzle_row[j] > puzzle_row[i]:
                    count_inversions += 1

        return count_inversions % 2 != 0

    def close(self, puzzle):
        return

    def solve(self):

        #self.puzzle = [item for sublist in self.puzzle for item in sublist]
        start = Board()
        start.set_puzzle(self.puzzle)
        self.push_open(start)

        while self.empty_open() is False:
            #print(len(self.open))
            #print(self.pop_open())
            current = self.pop_open()
            self.close.append(current.hash)

            if current.hash == self.end_hash:
                return current

            for n in current.neighbors():
                if n.hash in self.close:
                    continue
                n.h = self.heuristic(n.puzzle)
                if n.h <= self.min_open():
                     self.push_open(n)
        return start

    def find_elem_cord(self, el):
        for i in range(self.size):
            for j in range(self.size):
                if self.puzzle[i][j] == el:
                    return i, j

    def heuristic(self, pzl):
        h = 0
        for i in range(self.size):
            for j in range(self.size):
                i_p, j_p = self.find_elem_cord(pzl[i][j])
                h += abs(i - i_p) + abs(j - j_p)
        return h

if __name__ == "__main__":
    a = Algorithm(3)
    for i in a.puzzle_end_state:
        print(i)