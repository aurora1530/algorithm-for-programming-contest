n = int(input())
list_s = list(map(int, input().split()))
q = int(input())
list_t = list(map(int, input().split()))

count = 0

for t in list_t:
    if t in list_s:
        count += 1

print(count)
