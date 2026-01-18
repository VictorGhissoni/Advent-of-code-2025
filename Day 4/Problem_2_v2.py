import os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

f = open(os.path.join(__location__, 'input.txt'))
inp = f.read()
inp = inp.splitlines()

N_ROWS = len(inp)
N_COLS = len(inp[0])
for line in range(N_ROWS): #necessary conversion for the iterative version, strings are immutable
    inp[line] = list(inp[line])
count_matrix = [[0]*N_COLS for _ in range(N_ROWS)]
count = 0


DIRECTIONS  = [ #for adjacency
    (-1, 0),    #North
    (1, 0),     #South
    (0, -1),    #West
    (0, 1),     #East
    (-1, 1),    #North-East
    (-1, -1),   #North-West
    (1, 1),     #South-East
    (1, -1),    #South-West
]

def remove_paper(row, col, limit = 4):
    inp[row][col] = '.'
    global count
    count += 1
    for row_dir, col_dir in DIRECTIONS:
        new_row, new_col = row + row_dir, col + col_dir

        if not (0 <= new_row < N_ROWS and 0 <= new_col < N_COLS):
            continue

        if inp[new_row][new_col] == '@' and count_matrix[new_row][new_col] >= limit:
            count_matrix[new_row][new_col] -= 1
            if count_matrix[new_row][new_col] < limit:
                remove_paper(new_row, new_col, limit)

def count_neighbors(row, col, limit = 4):
    for row_dir, col_dir in DIRECTIONS:
        new_row, new_col = row + row_dir, col + col_dir

        if not (0 <= new_row < N_ROWS and 0 <= new_col < N_COLS):
            continue

        if inp[new_row][new_col] == '@':
            count_matrix[row][col] += 1

    if count_matrix[row][col]<limit: remove_paper(row, col, limit)

def forklift_papers(limit: int = 4):
    for row in range(N_ROWS):
        for col in range(N_COLS):
            if inp[row][col] == '@':
                count_neighbors(row, col, limit = 4)
    return count




print(f"forklift_papers = {forklift_papers(4):,}")


