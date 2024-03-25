def GCD(a: int, b: int) -> int:
    if b == 0:
        return a
    return GCD(b, a % b)


[x, y] = map(int, input().split())

print(GCD(x, y))
