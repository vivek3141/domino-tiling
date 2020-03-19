def fib(n):
    f1 = 1
    f2 = 1
    f3 = 1
    for i in range(n):
        f3 = f1 + f2
        f1 = f2
        f2 = f3
    return f3


def tiling2(m):
    return fib(m-1)


for i in range(1, 6):
    print(f"The number of ways to tile a 2 x {i} grid is {tiling2(i)}")
