n = int(input())
r1 = int(input())
r2 = int(input())
minimum = min(r1, r2)
diff_max = r2-r1

for _ in range(n-2):
    r = int(input())
    diff = r - minimum
    if diff_max < diff:
        diff_max = diff
    if minimum > r:
        minimum = r

print(diff_max)
