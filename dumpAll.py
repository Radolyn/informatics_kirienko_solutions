import os
from utils import debug

ranges = [
    [
        {'letter': 'A', 'range': '3443-3450', 'folder': '1 раздел'}
    ],
    [
        {'letter': 'A', 'range': '3455-3535', 'folder': '2 раздел'}
    ],
    [
        {'letter': 'A', 'range': '3501-3527', 'folder': '3 раздел'}
    ],
    [
        {'letter': 'A', 'range': '3528-3553', 'folder': '4 раздел'}
    ],
    [
        {'letter': 'A', 'range': '3608-3629', 'folder': '5 раздел'}
    ],
    [
        {'letter': 'A', 'range': '3735-3748', 'folder': '6 раздел'}
    ],
    [
        {'letter': 'A', 'range': '3642-3667', 'folder': '7 раздел'}
    ],
    [
        {'letter': 'A', 'range': '3791-3815', 'folder': '8 раздел'}
    ],
    [
        {'letter': 'A', 'range': '3828-3853', 'folder': '9 раздел'}
    ],
    [
        {'letter': 'A', 'range': '3828-3853', 'folder': '10 раздел'}
    ],
    [
        {'letter': 'A', 'range': '4179-4197', 'folder': '11 раздел'},
        {'letter': 'T', 'range': '112666-112672', 'folder': '11 раздел'}
    ],
    [
        {'letter': 'A', 'range': '111152-111177', 'folder': '12 раздел'}
    ],
    [
        {'letter': 'A', 'range': '111300-111325', 'folder': '13 раздел'}
    ],
    [
        {'letter': 'A', 'range': '111194-111220', 'folder': '14.1 раздел'},
        {'letter': 'A', 'range': '111362-111387', 'folder': '14.2 раздел'}
    ],
    [
        {'letter': 'A', 'range': '111326-111361', 'folder': '15 раздел'}
    ],
    [
        {'letter': 'A', 'range': '3749-3774', 'folder': '16 раздел'},
        {'letter': 'AA', 'range': '113078-113078', 'folder': '16 раздел'}
    ]
]

for item in ranges:
    for r in item:
        cmd = 'python parser.py --folder "%s" --range %s --letter %s' % (r['folder'], r['range'], r['letter'])

        if debug:
            print(cmd)

        os.system(cmd)
