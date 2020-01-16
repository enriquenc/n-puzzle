

class Algorithm:
    def __init__(self, puzzle, size):
        self.puzzle_end_state = self.get_end_puzzle_state(size)
        self.puzzle = puzzle
        self.size = size

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


if __name__ == "__main__":
    a = Algorithm(3)
    for i in a.puzzle_end_state:
        print(i)