import os

from utils import debug, ranges

for item in ranges:
    for r in item:
        cmd = 'python parser.py --folder "%s" --range %s --letter %s' % (
            r['folder'], r['range'], r['letter'])

        if debug:
            print(cmd)

        os.system(cmd)
