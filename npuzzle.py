from puzzle_parser import *
from algorithm import Algorithm


def main():
    parser = Parser()
    parser.find_size()

    a = Algorithm(parser.get_puzzle(), parser.size)


if __name__ == "__main__":
    main()
