from collections import Counter #https://www.geeksforgeeks.org/python-counter-objects-elements/
from  datetime import datetime
from functools import lru_cache #https://www.geeksforgeeks.org/python-functools-lru_cache/

@lru_cache(maxsize=None)
def calculate(item):
    if item == 0:
        return [1]
    else:
        digits = str(item)
        mid, odd = divmod(len(digits), 2) #https://www.w3schools.com/python/ref_func_divmod.asp
        if odd:
            return [item * 2024]
        else:
            return [int(digits[:mid]),int(digits[mid:])]

def blink(counts, times):
    for _ in range(times):
        new = Counter()
        for item, occurences in counts.items():
            for newitem in calculate(item):
                new[newitem] += occurences
        counts = new
    return counts

start = datetime.now()
# input = [125,17]
# cycles = 25
input = [64599,31,674832,2659361,1,0,8867,321]
cycles = 75
counts = Counter(input)
counts = blink(counts,cycles)
print(sum(counts.values()))
print(f"Finished in {datetime.now() - start} seconds")
