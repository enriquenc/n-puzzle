from os import walk, system
import re

my_path = './resources/'
r = re.compile("\d{1,}")
#os.system("python  puzzle_generator.py 6 -s -i 100 > file ")

for (dirpath, dirnames, filenames) in walk(my_path):
    print(dirpath)
    f = r.findall(dirpath)
    if f:
        size = f[0]
        solvable = ""
        if "unsolvable" in dirpath:
            solvable = "-u"
        else:
            solvable = "-s"
        for i in range(10):
            if size == 17 and i > 1:
                break
            system("python puzzle_generator.py " + size + " " + solvable + " -i " + str((i + 1) * 10) + " > " + dirpath + "/test_" + str(i + 1))
if "solvable" in "./resources/solvable/17x17":
    print('ok')