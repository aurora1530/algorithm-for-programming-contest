import copy


def insertion_sort(inputArray, g, cnt: int):
    array = copy.deepcopy(inputArray)
    length = len(array)
    for i in range(g, length):
        v = array[i]
        j = i-g
        while j >= 0 and v < array[j]:
            array[j+g] = array[j]
            j -= g
            cnt += 1
        array[j+g] = v
    return [array, cnt]


def shellSort(inputArray):
    array = copy.deepcopy(inputArray)
    cnt = 0
    G = []
    i = 1
    while True:
        G.append(i)
        i = 3 * i + 1
        if i > len(array):
            break
    G.reverse()
    for j in range(0, len(G)):
        [array, cnt] = insertion_sort(array, G[j], cnt)
    return [array, len(G), G, cnt]


n = int(input())
A = [int(input()) for _ in range(n)]
[sortedArray, m, G, cnt] = shellSort(A)

print(m)
print(' '.join(map(str, G)))
print(cnt)
for a in sortedArray:
    print(a)
