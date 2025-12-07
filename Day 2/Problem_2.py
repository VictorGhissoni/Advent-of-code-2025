import os
import math
import time
start_time = time.time()

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

f = open(os.path.join(__location__, 'input.txt'))
inp = f.read()
inp = inp.split(sep= ',')
#print(inp)

def divisors(n):
    div = set()
    for i in range(1,int(math.sqrt(n)) + 1):
        if (n%i == 0):
            div.add(i)
            div.add(n//i)
    div.remove(1)
    return sorted(list(div), reverse=True)

def str_splitter(s, split_size):
    ret = []
    start, end = 0, split_size
    for i in range(len(s)//split_size):
        ret.append(s[start:end])
        start, end = end, end + split_size
    return ret

def invalid_ids(input):
    count = 0
    is_invalid = False
    word_size = -1
    for ranges in input:
        start_range, end_range = ranges.split(sep='-')
        #print(start_range)
        #print(end_range)
        for num in range(int(start_range), int(end_range) + 1):
            word = str(num)
            if (word_size != len(word)):
                word_size = len(word)
                divisors_list = divisors(word_size)
                #print(divisors_list)
            for div in divisors_list:
                chunk_size = word_size//div
                if(len(set(str_splitter(word,chunk_size))) != 1):
                    continue
                is_invalid = True
                break
            if (is_invalid == True):
                #print(f"invalid id = {num}")
                is_invalid = False
                count += num
    return count

print(f"{invalid_ids(inp):,}")
print("--- %s seconds ---" % (time.time() - start_time))