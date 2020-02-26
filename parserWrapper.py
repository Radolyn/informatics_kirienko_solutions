import os
import sys

from utils import debug, ranges

try:
    rng = ranges[int(sys.argv[1]) - 1]
except:
    print('Неверный параметр.')
    exit(68)

for r in rng:
    cmd = 'python parser.py --folder "%s" --range %s --letter %s' % (
        r['folder'], r['range'], r['letter'])
    if debug:
        print(cmd)

    os.system(cmd)
