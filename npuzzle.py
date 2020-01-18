from puzzle_parser import *
from algorithm import *
from error import *


def main():
    parser = Parser()
    parser.find_size()

    a = Algorithm(parser.get_puzzle(), parser.size)
    if a.is_already_solved():
        success(Success.ALREADY_SOLVED)
    v = a.solve()
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

if __name__ == "__main__":
    main()
