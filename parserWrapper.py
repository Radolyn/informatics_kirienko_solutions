import os
import sys

from utils import debug, ranges, is_authorized, print_unauthorized

try:
    problems = ranges[int(sys.argv[1]) - 1]
except:
    print('Неверный параметр.')
    exit(68)

if not is_authorized():
    print_unauthorized()

for problem in problems:
    cmd = 'python parser.py --folder "%s" --range %s --letter %s' % (
        problem['folder'], problem['range'], problem['letter'])
    if debug:
        print(cmd)

    os.system(cmd)
