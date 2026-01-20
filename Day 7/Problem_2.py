import os
from functools import cache

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

f = open(os.path.join(__location__, 'input.txt'))
inp = f.read()
inp = inp.splitlines()

for i in range(len(inp)):
    if i%2!= 0:
        inp[i] = [*inp[i]] 

inp = [list(row) for row in zip(*inp)]

def print_tree(entry):
    entry = [list(row) for row in zip(*entry)]
    entry = ["".join(entry[i]) for i in range(len(entry))]
    print("entry = ")
    count = 0
    for i in range(len(entry)):
        count += entry[i].count('^')
        print(entry[i])
    return count

@cache
def send_beam(col_idx:int, line_idx:int):
    try:
        idx = inp[col_idx].index('^', line_idx)
    except ValueError:
        idx = -1
    result = 0
    if(idx != -1):
        result += 1
        result += send_beam(col_idx - 1, idx)
        result += send_beam(col_idx + 1, idx)
    return result

def find_start():
    result = 1
    for idx in range(len(inp)):
        if(inp[idx][0] == 'S'):
            result += send_beam(idx, 1)
            break
    return result

print(f"find_start = {find_start():,}")