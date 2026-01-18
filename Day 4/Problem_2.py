import os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

f = open(os.path.join(__location__, 'input.txt'))
inp = f.read()
inp = inp.splitlines()


def add_adj(row, col, count_matrix, n_rows, n_cols):
    
    WEST_TEST = (col - 1 >= 0)
    EAST_TEST = (col + 1 < n_cols)
    NORTH_TEST = (row - 1 >= 0)
    SOUTH_TEST = (row + 1 < n_rows)
    
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


def count_adjacent_papers(lim, input, count_matrix, n_rows, n_cols):
    for row in range(n_rows):
        for col in range(n_cols):
            if input[row][col] == '@':
                add_adj(row,col, count_matrix, n_rows, n_cols)
            else:
                count_matrix[row][col]+=lim

def count_viable(lim, input):
    
    n_cols = len(input[0])
    n_rows = len(input)
    count_matrix = [[0]*n_cols for _ in range(n_rows)]
    new_board = [['.']*n_cols for _ in range(n_rows)]
    
    count_adjacent_papers(lim, input, count_matrix, n_rows, n_cols)
    result = 0
    for row in range(n_rows):
        for col in range(n_cols):
            if input[row][col] == '@':
                if count_matrix[row][col] < lim:
                    result += 1
                else:
                    new_board[row][col] = '@'
    if result == 0:
        return result
    return result + count_viable(4, new_board)

#really unhappy with this one, would like to do without recursion

print(f"count_viable = {count_viable(4, inp)}")


