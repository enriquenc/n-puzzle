import argparse
import fileinput
import sys
  
parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('-f', dest="filename", type=str, help='file with puzzle')
parser.add_argument('-s', dest="save", type=str, help="save all comments to the file")
parser.add_argument('-v', dest="visualization", action="store_true", help="show the solve using gui")
parser.add_argument('-u', dest="heuristic", type=int, help="use different heuristic function. "
                                                    "1 - manhattan, "
                                                    "2 - chiponpos, "
                                                    "3 - euclidist. "
                                                    "Default: manhattan.", choices=range(1, 4))

args = parser.parse_args()
# if args.filename is not None:
#     sys.argv[1] = args.filename

# print(args.heuristic)

# counter = 0
# for line in fileinput.input():
#     line = line.rstrip()
#     if counter == 5:
#         break
#     if args.save is not None:
#         splited = line.split('#')
#         if len(splited) > 1:
#             print(splited[1])
#     else:
#         print(line)
#     counter += 1
 
