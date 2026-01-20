import os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

f = open(os.path.join(__location__, 'input.txt'))
inp = f.read()
inp = inp.splitlines()


for i in range(len(inp)):
    inp[i] = [*inp[i]] 


inp = [list(row) for row in zip(*inp)] #transposing for better cache acess with spatial locality


def print_tree(inp):
    inp = [list(row) for row in zip(*inp)]
    inp = ["".join(inp[i]) for i in range(len(inp))]
    print("inp = ")
    for i in range(len(inp)):
        print(inp[i])

def send_beam(col, col_idx, line_idx):
    idx = line_idx
    result = 0
    for char in col:
        if (char== '^'):
            result += 1
            result += send_beam(inp[col_idx-1][idx:], col_idx - 1, idx)# no boundary checking, unecessary for this input
            result += send_beam(inp[col_idx+1][idx:], col_idx + 1, idx)# no boundary checking, unecessary for this input
            return result
        elif (char== '.'):
            inp[col_idx][idx] = '|'
            #if(input("Press c to continue: ") != "c"):
                #return result
            #print_tree(inp)            
            idx += 1
        elif (char== '|'):
            return result
    return result

def find_start():
    result = 0
    for idx in range(len(inp)):
        if(inp[idx][0] == 'S'):
            result += send_beam(inp[idx][1:], idx, 1)
            break
    return result

print(f"find_start = {find_start():,}")