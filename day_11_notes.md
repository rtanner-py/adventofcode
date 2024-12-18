# Notes for day 11 on new things

## from collections import Counter
https://www.geeksforgeeks.org/python-counter-objects-elements/
Counter is a sub-class which is used to count hasbale objects. Creates a hash table of an iterable when involved.
If using a list as an iterable data container:
a = [12,3,4,3,5,11,12,6,7]
x = Counter(a)
print(x) will return a dictionary of key, value pairs indicating the item (like 12) and the number of times it occurs (2)

## from functools import lru_cache
https://www.geeksforgeeks.org/python-functools-lru_cache/
lru_cache helps iin reducing the execution time of the function by using memoization
if maxsize=None, the cache can grow without any limitations
can use typed=True/False. If set to true, will cache different data types separately (3 and 3.0 would be treated as distinct calls with distint results)
To use, decorate a function call with @lru_cache(maxsize=None)

## divmod(dividend, divisor)
https://www.w3schools.com/python/ref_func_divmod.asp
Returns a tuple containing the quotient and the remainder when the dividend is divded by the divisor
result, odd = divmod(5,2) would return (2,1)
1 equates to True, 0 equates to false
