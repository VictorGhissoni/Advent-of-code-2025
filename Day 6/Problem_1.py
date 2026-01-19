import os
from functools import reduce

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

f = open(os.path.join(__location__, 'input.txt'))
inp = f.read()
inp = inp.splitlines()

#print(f"inp = {inp}")

for i in range(len(inp)):
    inp[i] = inp[i].split()

#print(f"inp = {inp}")

inp = [list(reversed(row)) for row in zip(*inp)] #transposing for better cache acess with spatial locality

def homework(numbers, operation):
    match operation:
        case '+':
            return reduce(lambda x, y: int(x) + int(y), numbers)
        case '*':
            return reduce(lambda x, y: int(x) * int(y), numbers)
        
def Sum_it_all(entry):
    results = [homework(line[1:],line[0]) for line in entry]
    return homework(results, '+')

print(f"Sum_it_all = {Sum_it_all(inp):,}")