n = int(input())
r1 = int(input())
r2 = int(input())
minimum = min(r1, r2)
diff_max = r2-r1

for _ in range(n-2):
    r = int(input())
    diff_max = max(diff_max, r-minimum)
    minimum = min(minimum, r)

print(diff_max)
