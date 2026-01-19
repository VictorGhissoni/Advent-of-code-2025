import os
from functools import reduce

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

f = open(os.path.join(__location__, 'input.txt'))
inp = f.read()
inp = inp.splitlines()

inp = [list(row) for row in zip(*inp)] #transposing for better cache acess with spatial locality

def homework(numbers, operation):
    match operation:
        case '+':
            return reduce(lambda x, y: x + y, numbers)
        case '*':
            return reduce(lambda x, y: x * y, numbers)

def parse_entrys(entry):
    result = 0
    SIZE = len(entry[0])
    for col in entry:
        if(col[-1] == '+' or col[-1] == '*'):
            op = col[-1]
            nums = []
        num = ''
        for char in col:
            if (char.isdigit()):
                num+=char
        if(num != ''):
            nums.append(int(num))
        if(col == [' ']*SIZE):
            #print(f"nums = {nums}")
            #print(f"op = {op}")
            result += homework(nums, op)
    result += homework(nums, op)
    return result
        
print(f"parse_entrys = {parse_entrys(inp)}")
