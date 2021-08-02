from itertools import count
def fact(n):
    result = 1
    for el in count(1):
        if el <= n:
            result *= el
            yield result
        else:
            break

for el in fact(4):
    print(el)