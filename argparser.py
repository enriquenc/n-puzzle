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
