import os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

f = open(os.path.join(__location__, 'input.txt'))
inp = f.read()
inp = inp.split()

def safe(input):
    start = 50
    count = 0
    for instruction in input:
        #print(instruction)
        num = int(instruction[1:])
        #print(num)
        match instruction[:1].startswith("L"):
            case True:
                start = start - num
            case _:
                start = start + num
         
        start = start%100
        if (start == 0):
            count+=1
    return count

print(safe(inp))