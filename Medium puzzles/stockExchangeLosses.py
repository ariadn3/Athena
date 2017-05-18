highestPoint = -1
biggestLoss = 0

n = int(input())
for i in input().split():
    v = int(i)
    if v > highestPoint:
        highestPoint = v
    elif v-highestPoint < biggestLoss:
        biggestLoss = v-highestPoint

print(biggestLoss)