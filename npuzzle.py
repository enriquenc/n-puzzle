from puzzle_parser import *
from algorithm import *
from error import *
import time

def main():

    # puzzle = [[1, 2, 3],
    #           [0, 8, 4],
    #           [7, 6, 5]]
    #
    # puzzle1 = [[5, 7, 1],
    #            [6, 0, 2],
    #            [4, 3, 8]]
    #
    # puzzle2 = [[1, 5, 3],
    #            [2, 0, 4],
    #            [6, 8, 7]]
    #
    # puzzle4 = [[1, 3, 6, 4],
    #            [5, 2, 12, 8],
    #            [15, 13, 7, 14],
    #            [11, 10, 0, 9]]

    # puzzle = []
    # f = open("file", 'r')
    # size = int(f.readline())
    # for i in range(size):
    #     line = f.readline().strip(' \n')
    #     line = line.split(' ')
    #     a = []
    #     for j in line:
    #         a.append(int(j))
    #     puzzle.append(a)
    parser = Parser()
    parser.get_input()
    a = Algorithm(parser.puzzle, parser.size)
    if a.is_already_solved():
        success(Success.ALREADY_SOLVED)
    #if a.is_solvable() is False:
    #    print('kek')
    #    return

    before = time.time()
    v = a.solve()
    after = time.time()

    answer = []
    for l in v.puzzle:
        print(l)
    print('\n\n')
    while v.parent:
        answer.append(v.puzzle)
        v = v.parent
    answer.append(v.puzzle)
    length = len(answer)
    while len(answer) != 0:
        p = answer.pop()
        for l in p:
            print(l)
        print(' ')
    print(length)
    print(after - before)

if __name__ == "__main__":
    main()
