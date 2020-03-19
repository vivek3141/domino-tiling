from math import cos, sin, sqrt, pi

# closed form


def tiling(m, n):
    if m * n % 2 != 0:
        return 0
    ret = 1
    for k in range(1, m + 1):
        for l in range(1, n + 1):
            term = sqrt(4 * (cos(k * pi/(m + 1))) ** 2 +
                        4 * (cos(l * pi/(n + 1))) ** 2)
            ret *= term
    return sqrt(ret)


for i in range(1, 6):
    print(
        f"The number of ways to tile a 2 x {i} grid is {int(tiling(2, i) + 0.5)}")

print(f"The number of ways to tile a 4 x 4 grid is {int(tiling(4, 4) + 0.5)}")
