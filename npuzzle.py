from puzzle_parser import *
from algorithm import Algorithm


def main():
    parser = Parser()
    parser.find_size()

    a = Algorithm(parser.get_puzzle(), parser.size)
    print(a.puzzle)
    print(a.puzzle_end_state)


if __name__ == "__main__":
    main()
