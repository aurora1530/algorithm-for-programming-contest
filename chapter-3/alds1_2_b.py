N = int(input())
A = list(map(int, input().split()))

switch_count = 0
for i in range(N):
    minIndex = i
    for j in range(i, N):
        if A[j] < A[minIndex]:
            minIndex = j
    [A[i], A[minIndex]] = [A[minIndex], A[i]]
    switch_count += 1 if minIndex != i else 0

print(' '.join(map(str, A)))
print(switch_count)
