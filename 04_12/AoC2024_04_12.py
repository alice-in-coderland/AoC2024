import numpy as np
import re

# %%
letters = '''MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX'''
# %%

with open('input_04_12.txt', 'r') as f:
    letters = f.read()

# %%

# PART 1
letters_ar = np.array([list(line) for line in letters.splitlines()])

XMAS_times = 0

for _ in range(2):
    # find non-diagnonals
    for row in letters_ar:
        XMAS_times += len(re.findall(r'XMAS', ''.join(row)))
        XMAS_times += len(re.findall(r'SAMX', ''.join(row)))
    # find diagonals:
    x, y = letters_ar.shape
    if x != y:
        print('matrix not square')
    else:
        for i in range(0 - x, x):
            XMAS_times += len(re.findall(r'XMAS', ''.join(letters_ar.diagonal(i))))
            XMAS_times += len(re.findall(r'SAMX', ''.join(letters_ar.diagonal(i))))
    letters_ar = np.rot90(letters_ar)

print(f'XMAS appears {XMAS_times} times.')

# %%

# PART 2
import numpy.ma as ma

letters_ar = np.array([list(line) for line in letters.splitlines()])
m = [[0, 1, 0], [1, 0, 1], [0, 1, 0]]
X_MAS = ma.array([['M', '.', 'S'],
                  ['.', 'A', '.'],
                  ['M', '.', 'S']], mask=m)

X_MAS_times = 0

x, y = letters_ar.shape
if x != y:
    print('matrix not square')
else:
    for i in range(y - 2):
        for j in range(x - 2):
            subarray = ma.array([letters_ar[i:i + 3, j:j + 3]], mask=m)
            for _ in range(4):
                if ma.allequal(X_MAS, subarray):
                    X_MAS_times += 1
                X_MAS = np.rot90(X_MAS)

print(f'X-MAS appears {X_MAS_times} times.')
#%%
