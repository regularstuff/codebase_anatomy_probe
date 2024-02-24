"""Four ways to get triancle nbs"""

def tri1(n):
    total = 0
    for x in range(n + 1):
        for y in range(x):
            total += 1
    return total

def tri2(n):
    total = 0
    for x in range(n + 1):
        total += x
    return total

def tri3(n):
    return sum(range(n + 1))

def tri4(n):
    return n * (n + 1) // 2