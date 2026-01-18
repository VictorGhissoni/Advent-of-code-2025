import os
import itertools

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

f = open(os.path.join(__location__, 'input.txt'))
inp = f.read()
inp = inp.splitlines()

n_cols = len(inp[0])
n_rows = len(inp)
count_matrix = [[0]*n_cols for _ in range(n_rows)]

def add_adj(row, col):
    
    COL_INF_BOUND = (col - 1 >= 0)
    COL_SUP_BOUND = (col + 1 < n_cols)
    ROW_INF_BOUND = (row - 1 >= 0)
    ROW_SUP_BOUND = (row + 1 < n_rows)
    
    NORTH_TEST = ROW_INF_BOUND
    SOUTH_TEST = ROW_SUP_BOUND
    WEST_TEST = COL_INF_BOUND
    EAST_TEST = COL_SUP_BOUND
    
    NORTH_EAST_TEST = NORTH_TEST and EAST_TEST
    NORTH_WEST_TEST = NORTH_TEST and WEST_TEST
    SOUTH_EAST_TEST = SOUTH_TEST and EAST_TEST
    SOUTH_WEST_TEST = SOUTH_TEST and WEST_TEST

    if NORTH_TEST: count_matrix[row - 1][col] += 1
    if SOUTH_TEST: count_matrix[row + 1][col] += 1
    if WEST_TEST: count_matrix[row][col - 1] += 1
    if EAST_TEST: count_matrix[row][col + 1] += 1
    if NORTH_EAST_TEST: count_matrix[row - 1][col + 1] += 1
    if NORTH_WEST_TEST: count_matrix[row - 1][col - 1] += 1
    if SOUTH_EAST_TEST: count_matrix[row + 1][col + 1] += 1
    if SOUTH_WEST_TEST: count_matrix[row + 1][col - 1] += 1


def count_adjacent_papers(lim):
    for row in range(n_rows):
        for col in range(n_cols):
            if inp[row][col] == '@':
                add_adj(row,col)
            else:
                count_matrix[row][col]+=lim

def count_viable(lim):
    count_adjacent_papers(lim)
    #print(f"count_matrix = \n{count_matrix}")
    result = 0
    for n in itertools.chain.from_iterable(count_matrix):
        if n < 4:
            result += 1
    return result

print(f"count_viable = {count_viable(4)}")


