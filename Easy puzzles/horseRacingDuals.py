import math

n = int(input())
p = [int(input()) for i in range(n)]
p.sort()
diff = math.inf
for i in range(1, n):
    if p[i]-p[i-1]<diff: diff = p[i]-p[i-1]
    if not diff: break

print(diff)