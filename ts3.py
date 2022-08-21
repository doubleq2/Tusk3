import collections
from functools import lru_cache
import timeit

@lru_cache(maxsize=15)
def my(string):
    start = timeit.timeit()
    c = collections.Counter()
    for word in list(string):
        c[word] += 1
    end = timeit.timeit()
    print(end - start)
    return len(c)
print(my("aasddsjfhsjdflsdjkfhljskdflhjsdhdfljksdjlkfshldjkfhjlksdhjklfhjslkdfljhksdjhlkfsdjhkfhjksdfhjsdjhfsjhkdfhjksdfjhk"))