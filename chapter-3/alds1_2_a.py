N = int(input())
A = list(map(int, input().split()))

shouldSort = True
switch_count = 0
while shouldSort:
    shouldSort = False
    for j in range(N-1, 0, -1):
        if A[j] < A[j-1]:
            [A[j], A[j-1]] = [A[j-1], A[j]]
            switch_count += 1
            shouldSort = True
print(' '.join(map(str, A)))
print(switch_count)
