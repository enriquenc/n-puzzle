#from puzzle_parser import *
from algorithm import *
from error import *
import time

def main():
    #parser = Parser()
    #parser.find_size()
    puzzle = [[1, 2, 3],
              [0, 8, 4],
              [7, 6, 5]]

    puzzle1 = [[5, 7, 1],
               [6, 0, 2],
               [4, 3, 8]]

    puzzle2 = [[1, 5, 3],
               [2, 0, 4],
               [6, 8, 7]]

    size = 3

    a = Algorithm(puzzle2, size)
    if a.is_already_solved():
        success(Success.ALREADY_SOLVED)
    if a.is_solvable() is False:
        print('kek')
        return

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
