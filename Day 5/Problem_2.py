import os


__location__ = os.path.realpath(
os.path.join(os.getcwd(), os.path.dirname(__file__)))

f = open(os.path.join(__location__, 'input.txt'))
inp = f.read()
inp = inp.splitlines()

ranges = []
for line in inp:
    if(len(line) == 0): 
        break
    ranges.append(line)

def sorting_order(element):
    w1, w2 = element.split('-')
    return (int(w1),int(w2))

def reducing_ranges(ranges):
    i = 0
    ranges_size = len(ranges)
    while(True):
        start, end = ranges[i].split('-')
        start, end = int(start), int(end)   
        next_start, next_end = ranges[i+1].split('-')
        next_start, next_end = int(next_start), int(next_end)

        if (next_start<=end or next_start == end + 1):
            if (next_end<=end):
                ranges.pop(i+1)
                ranges_size = len(ranges)
            else:
                ranges.pop(i+1)
                ranges[i] = str(start) + '-' + str(next_end)
                ranges_size = len(ranges)
            if (i+1==ranges_size):
                break
        else:
            i+=1
            if (i+1==ranges_size):
                break



def count_fresh(ranges):
    count = 0
    for ran in ranges:
        start, end = ran.split('-')
        start, end = int(start), int(end)
        count += end - start + 1
    return count


ranges = sorted(ranges, key=sorting_order)
reducing_ranges(ranges)

print(f"count_fresh = {count_fresh(ranges):,}")
