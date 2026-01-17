import os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

f = open(os.path.join(__location__, 'input.txt'))
inp = f.read()
inp = inp.split(sep= ',')
#print(inp)


def invalid_ids(input):
    count = 0
    for inp in input:
        start, end = inp.split(sep='-')
        #print(start)
        #print(end)
        for i in range(int(start), int(end) + 1):
            word = str(i)
            if(len(word)%2 != 0):
                continue
            #print(word)
            #print(type(len(word)))
            if(word[0:(len(word)//2)] == word[(len(word)//2):]):
                count += i
    return count

print(f"count = {invalid_ids(inp):,}")