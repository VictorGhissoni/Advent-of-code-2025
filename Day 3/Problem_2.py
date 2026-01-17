import os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

f = open(os.path.join(__location__, 'input.txt'))
inp = f.read()
inp = inp.splitlines()
#print(inp)

def highlight_index(data_list, index_to_highlight):
    # ANSI color codes
    COLOR_RED = '\033[91m'  # Red text
    COLOR_END = '\033[0m'   # Reset color to default

    highlighted_list = []
    for i, item in enumerate(data_list):
        if i == index_to_highlight:
            # Wrap the specific item in color codes
            highlighted_list.append(f"{COLOR_RED}{item}{COLOR_END}")
        else:
            highlighted_list.append(str(item))

    print(f"[{', '.join(highlighted_list)}]")

def find_n_max(l: list, n:int):
    new_list = set(l)
    while(n>0):
        m = max(new_list)
        new_list.remove(m)
        n= n-1
    return m

def largest_jolt_NoTCO(line, n = 2):
    msg = ''
    depth = 1
    
    while (True):
        if n == 0:
            return msg
        m = max(line)
        #highlight_index(line, line.index(m))
        #print(f"len(line) = {len(line)}, index = {line.index(m)}, len(line) - index -1= {len(line)-line.index(m)-1}, n = {n}, max = {m}")
        while(len(line) - line.index(m)<n):
            depth+=1
            m = find_n_max(line, depth)
        idx = line.index(m)
        depth=1
        line = line[idx+1:]
        msg += m
        n = n-1
    

def sum_banks(inp):
    result = 0
    for bank in inp:
        tmp = int(largest_jolt_NoTCO(list(bank), n = 12))
        #print(f"tmp = {tmp:,}")
        # if input("press c to continue\n")!= "c":
        #     break
        # print("="*100)
        result += tmp
    return result

print(f"sum_banks = {sum_banks(inp):,}")



    
