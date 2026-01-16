import os
import time
start_time = time.time()

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

f = open(os.path.join(__location__, 'input.txt'))
inp = f.read()
inp = inp.split(sep= ',')

def is_repeated(s,n):
    if (n > len(s) or len(s)%n!=0):
        return False
    blocks = []
    start = 0
    end = start + len(s)//n
    for _ in (range(n)):
        blocks.append(s[start:end])
        start = end
        end = start + len(s)//n
    return len(set(blocks)) == 1

def next_repeated(s:str, n:int, lim: int):
    if (len(s)%n!= 0):
        new_word = "1" + "0"*len(s)
        if (int(new_word)>lim):
            return new_word
        return next_repeated(new_word, n, lim)
    blocks = []
    start = 0
    end = start + len(s)//n
    for _ in (range(n)):
        blocks.append(s[start:end])
        start = end
        end = start + len(s)//n
    for i in range(len(blocks)):
        blocks[i] = int(blocks[i])
    new_word = str(blocks[0])*n
    if (int(new_word)<=int(s)):
        new_word = str(blocks[0]+1)*n
    return new_word

def sieve(n):
    if n < 2:
        return []

    primes = [True] * (n + 1)
    primes[0] = primes[1] = False  # 0 and 1 aren't prime

    p = 2
    while (p * p <= n):
        if (primes[p] == True):
            for i in range(p * p, n + 1, p):
                primes[i] = False
        p += 1

    prime_list = []
    for p in range(n + 1):
        if primes[p]:
            prime_list.append(p)

    return prime_list

def invalid_ids(input):
    count = 0
    for inp in input:
        start, end = inp.split(sep='-')
        n_check = sieve(int(len(end)))
        for n in n_check:
            if (is_repeated(start,n)):
                count += int(start)
                break
        next_candidates = {}
        for n in n_check:
            next_candidates[n] = int(next_repeated(start,n, int(end)))
        minimum = min(next_candidates.values())
        while (minimum <= int(end)):
            count += minimum
            divs = [key for key, value in next_candidates.items() if value == minimum]
            for div in divs:
                next_candidates[div] = int(next_repeated(str(minimum), div, int(end)))
            minimum = min(next_candidates.values())
    return count

#Possible better perfomance in cases where there's plenty divisors for our word lenght?
def invalid_ids_v3(input): 
    count = 0
    for inp in input:
        start, end = inp.split(sep='-')
        n_check = sieve(int(len(end)))
        for n in n_check:
            if (is_repeated(start,n)):
                count += int(start)
                break
        next_candidates = {}
        for n in n_check:
            tmp = int(next_repeated(start,n, int(end)))
            if (tmp<=int(end)):
                next_candidates[n] = tmp
        if(len(next_candidates) == 0):
            continue
        minimum = min(next_candidates.values())
        while (True):
            count += minimum
            divs = [key for key, value in next_candidates.items() if value == minimum]
            for div in divs:
                tmp = int(next_repeated(str(minimum), div, int(end)))
                if (tmp<=int(end)):
                    next_candidates[div] = tmp
                else:
                    next_candidates.pop(div)
            if (len(next_candidates) == 0):
                break
            minimum = min(next_candidates.values())
    return count

print(f"count = {invalid_ids(inp):,}")
print("--- %s seconds ---" % (time.time() - start_time))