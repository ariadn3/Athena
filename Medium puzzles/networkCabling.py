import statistics

n = int(input())
x,y = [],[]

for i in range(n):
    xi, yi = [int(j) for j in input().split()]
    x.append(xi)
    y.append(yi)

median = statistics.median(y)
length = max(x)-min(x)
for i in y:
    length += abs(median-i)

print(int(length))