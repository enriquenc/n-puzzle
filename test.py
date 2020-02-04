import time
from algorithm import *
from puzzle_parser import *
from os import walk
import re

class Tests():

    @staticmethod
    def test_all():
        my_path = './resources/'
        r = re.compile("\dx\d")


        for (dirpath, dirnames, filenames) in walk(my_path):
            if filenames != []:
                d = r.findall(dirpath)

                print("\033[96m {}\033[00m".format('TEST FOR ' + d[0][0] + 'x' + d[0][0] + ' PUZZLES ' + dirpath[:-4].split('/')[2].upper() + '\n'))
                for file in filenames:
                    p = Parser()
                    p.get_input(dirpath + '/' + file)
                    before = time.time()
                    a = Algorithm(p.puzzle, p.size)
                    if a.is_solvable() is False:
                        print(file + ' - not solvable.')
                        continue
                    res = a.solve()
                    after = time.time()

                    if res.hash == a.end_hash:
                        print("\033[92m {}\033[00m".format(file + " - OK. Time - " + str(after - before) + '.'))
                    else:
                        print("\033[91m {}\033[00m".format(file + " - NOOK. Time - " + str(after - before) + '.'))
                    print('\t total opened nodes: ' + str(a.total_opened_nodes))
                    print('\t max nodes at the same time: ' + str(a.max_number_in_memory))
                    print('\t steps to solve: ' + str(a.solve_steps_amount))
                print('\n')


Tests.test_all()