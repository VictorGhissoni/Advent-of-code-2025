import os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

f = open(os.path.join(__location__, 'input.txt'))
inp = f.read()
inp = inp.split()

def safe(input):
    #input = input.split() #if you're using the test function this is necessary
    start = 50
    count = 0
    for instruction in input:
        num = int(instruction[1:])
        #print(f"pos = {start}")
        #print(f"instruction = {instruction}")
        #print(f"num = {num}")
        if (num >= 100):
            count += num//100
            #print(f"count = {count}")
            #print("==============================")
        match instruction[:1].startswith("L"):
            case True:
                if (start - num%100 <= 0 and start != 0):
                    count += 1
                    #print(f"count = {count}")
                    #print("==============================")
                start = start - num
            case _: 
                if (start + num%100 >= 100 and start != 0):
                    count += 1
                    #print(f"count = {count}")
                    #print("==============================")
                start = start + num
        start = start%100
        #print("")
    return count

print(safe(inp))

#Unit testing

tests = ["R49 L98","R49 R1","R49 R1 R1","R49 R1 L1","L50 L100","R50 R100","L50 L400","L50 R400","R1000", "L49 L101", "R49 R102"]
results = [0,1,1,1,2,2,5,5,10,2, 2]


tests_2 = ["L50 R100", "L50 R101", "L50 L102", "L50 R200", "L50 R1", "L50 L1", "R100", "R51" , "R150", "R50"]
results_2 = [2, 2, 2, 3, 1, 1, 1, 1, 2, 1]

def test_func(inp, f, cor):
    for i in range(len(inp)):
        result = f(inp[i])
        print(f"result = {result}")
        print(f"gabarito = {cor[i]}")
        assert result == cor[i], f"erro no teste {i}, input = {inp[i]}"


#test_func(tests, safe, results)
#test_func(tests_2,safe, results_2)