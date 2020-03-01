import os

from utils import debug, ranges, is_authorized, print_unauthorized

if not is_authorized():
    print_unauthorized()

for item in ranges:
    for r in item:
        cmd = 'python parser.py --folder "%s" --range %s --letter %s' % (
            r['folder'], r['range'], r['letter'])

        if debug:
            print(cmd)

        os.system(cmd)
