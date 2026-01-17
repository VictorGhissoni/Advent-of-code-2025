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
            highlighted_list.append(f"{COLOR_RED}{item}{COLOR_END}")
        else:
            highlighted_list.append(str(item))

    print(f"[{', '.join(highlighted_list)}]")

def largest_jolt_recursion(line:list , original:str , side: int, n:int = 2): #python doesn't use Tail Call Optimization
    #print(f"line start = {line}, n = {n}, original = {original}")
    if(n>0):
        m = max(line)
        #print(f"max = {m}")
        idx = line.index(m)
        if len(line)-line.index(m)-1>n:
            line = line[idx+1:]
            #print(f"line flow 1 = {line}")
            #add to the end
            new_side=1
        else:
            #add to the beggining
            line = line[:idx]
            #print(f"line flow 2 = {line}")
            new_side=0
        match side:
            case 0:
                msg=m+original
            case 1:
                msg=original+m
        return(largest_jolt_recursion(line, msg, new_side, n=n-1))
    return original


def largest_jolt_NoTCO(line, n = 2, original = ''):
    msg = ''
    side = -1
    
    while (True):
        if n == 0:
            return msg
        m = max(line)
        #print(f"max = {m}")
        idx = line.index(m)
        highlight_index(line, line.index(m))
        print(f"len(line) = {len(line)}, index = {line.index(m)}, len(line) - index -1= {len(line)-line.index(m)-1}, n = {n}, max = {m}")
        if len(line)-line.index(m)>=n:
            line = line[idx+1:]
            #print(f"line flow 1 = {line}")
            #add to the end
            new_side=1
        else:
            #add to the beggining
            line = line[:idx]
            #print(f"line flow 2 = {line}")
            new_side=0
        match side:
            case 0:
                msg=m+original
            case 1:
                msg=original+m
            case _:
                msg = m
        side = new_side
        original = msg
        n = n-1
    

def sum_banks(inp):
    result = 0
    for bank in inp:
        tmp = largest_jolt_NoTCO(list(bank))
        #tmp = largest_jolt_recursion(list(bank), original= "", side = 0)
        #print(f"tmp = {tmp}")
        # if input("press c to continue\n")!= "c":
        #     break
        result += int(tmp)
    return result

print(sum_banks(inp))



    
