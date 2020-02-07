from puzzle_parser import *
from algorithm import *
from error import *
import time
from argparser import args
import visualization
from tkinter import Tk


def default_output(answer_list, size):
    print('\nRESULT:\n')

    while len(answer_list) != 0:
        p = answer_list.pop()
        for i in range(len(p)):
            if p[i] == 0:
                print("\033[92m{}\033[00m".format("%3d"%p[i]), end='')
            else:
                print("%3d"%p[i], end='')
            # format ouput for each of puzzle elements
            if i % size == size - 1:
                print('') # put the \n in the end of puzzle line
        print(' ')


def visual_output(answer_list, size):
    v = visualization.Visualization(answer_list, size, master=Tk())
    v.mainloop()
    return


def print_answer(alogrithm):
    before = time.time()
    board_list = alogrithm.solve()
    # answer list of Board Class elements
    # from [input value] -> [end value]
    after = time.time()

    answer = []
    # create answer list only with puzzles
    while board_list.parent:
        answer.append(board_list.puzzle)
        board_list = board_list.parent
    answer.append(board_list.puzzle)

    length = len(answer)
    if args.visualization is False:
        default_output(answer, board_list.size)

    print("\033[92m {}\033[00m".format("\nPUZZLE SOLVED:"))
    print("\033[92m {}\033[00m".format("\nTotal opened nodes: " + str(alogrithm.total_opened_nodes)))
    print("\033[92m {}\033[00m".format("\nMax nodes at the same time: " + str(alogrithm.max_number_in_memory)))
    print("\033[92m {}\033[00m".format("\nSteps count: " + str(length - 1)))
    print("\033[92m {}\033[00m".format("\nTime to solve: " + str(after - before)))

    if args.visualization:
        visual_output(answer, board_list.size)


def main():
    parser = Parser()
    parser.get_input()
    a = Algorithm(parser.puzzle, parser.size)
    if a.is_already_solved():
        success(Success.ALREADY_SOLVED)
    if a.is_solvable() is False:
        error(Error.ERROR_NON_SOLVABLE_PUZZLE)
    print_answer(a)


if __name__ == "__main__":
    main()
