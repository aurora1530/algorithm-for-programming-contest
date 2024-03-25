import math


def isPrime(num: int) -> bool:
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    sqrt = math.ceil(math.sqrt(num))
    for i in range(3, sqrt+1, 2):
        if num % i == 0:
            return False
    return True


n = int(input())

count = 0
for _ in range(n):
    number = int(input())
    if isPrime(number):
        count += 1

print(count)
