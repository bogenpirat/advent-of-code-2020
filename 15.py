input = """0,14,1,3,7,9"""

input2 = """0,3,6"""

numbers = [int(x) for x in input.split(',')]

store = {} # lookup map for value => index
for i, val in enumerate(numbers[0:-1]):
    store[val] = i

for i in range(len(numbers), 30000000):
    prevNumber = numbers[i - 1]
    
    thisNumber = 0
    if prevNumber in store:
        prevIdx = store[prevNumber]
        thisNumber = (i - 1) - prevIdx

    store[numbers[i - 1]] = i - 1 # housekeeping

    numbers.append(thisNumber)

    # parts 1 & 2
    if i in [2020 - 1, 30000000 - 1]:
        print(f'{i+1}: {numbers[i]}')