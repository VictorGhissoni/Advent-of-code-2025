import os


__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

f = open(os.path.join(__location__, 'input.txt'))
inp = f.read()
inp = inp.splitlines()


ranges = []
for line in inp:
    if(len(line) == 0): 
        foods = inp[len(ranges)+1:]
        foods = [int(food) for food in foods]
        foods = sorted(foods)
        break
    ranges.append(line)
#print(f"len(ranges) = {len(ranges)}")
#print(f"foods = {foods}")

def sorting_order(element):
    w1, w2 = element.split('-')
    return (int(w1),int(w2))

#print(f"ranges = {ranges}")
#print(f"sorted(ranges) = {sorted(ranges, key=sorting_order)}")

def reducing_ranges(ranges):
    i = 0
    ranges_size = len(ranges)
    while(True):
        start, end = ranges[i].split('-')
        start, end = int(start), int(end)
        #print(f"(start, end) = {(start, end)}")     
        next_start, next_end = ranges[i+1].split('-')
        next_start, next_end = int(next_start), int(next_end)

        #print(f"(next_start, next_end) = {(next_start, next_end)}")
        if (next_start<=end or next_start == end + 1):#13-16 15-18
            if (next_end<=end):
                ranges.pop(i+1)
                ranges_size = len(ranges)
            else:
                ranges.pop(i+1)
                ranges[i] = str(start) + '-' + str(next_end)
                ranges_size = len(ranges)
            if (i+1==ranges_size):
                #print("cheguei ao fim")
                break
        else:
            i+=1
            if (i+1==ranges_size):
                #print("cheguei ao fim")
                break



def count_fresh(ranges, foods):
    i = 0
    j = 0
    size_foods = len(foods)
    size_ranges = len(ranges)
    count = 0
    while (True):
        start, end = ranges[i].split('-')
        start, end = int(start), int(end)
        if(foods[j]<=end):
            if(start<=foods[j]):
                count+=1
            if(j+1<size_foods):
                j= j+1
            else: break
        elif (i+1<size_ranges):
            i= i+1
        else: break
    return count


ranges = sorted(ranges, key=sorting_order)
reducing_ranges(ranges)

#print(f"ranges after reduction = {ranges}")
#print(f"after reduction len(ranges) = {len(ranges)}")

print(f"count_fresh = {count_fresh(ranges, foods)}")
