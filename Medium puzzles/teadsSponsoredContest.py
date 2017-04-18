import math

n = int(input())
adjDict = {}
adjList = []

for i in range(n):
    n1, n2 = [int(j) for j in input().split()]
    adjList.append((n1, n2))
    adjDict[n1] = set()
    adjDict[n2] = set()

for i in adjList:
    adjDict[i[0]].add(i[1])
    adjDict[i[1]].add(i[0])

minNkey = None
minNcount = math.inf
for i in adjDict.keys():
    if len(adjDict[i]) <= minNcount:
        minNcount = len(adjDict[i])
        minNkey = i

visitedSet = set()
maxIndex, maxDist = 0, 0
nodeList = [(i, 0)]
while nodeList:
    node, distance = nodeList.pop(0)
    if node in visitedSet:
        continue
    else:
        for i in adjDict[node]:
            nodeList.append((i, distance + 1))
        visitedSet.add(node)
        if distance > maxDist:
            maxIndex = node
            maxDist = distance

visitedSet = set()
maxDist = 0
nodeList = [(maxIndex, 0)]
while nodeList:
    node, distance = nodeList.pop(0)
    if node in visitedSet:
        continue
    else:
        for i in adjDict[node]:
            nodeList.append((i, distance + 1))
        visitedSet.add(node)
        if distance > maxDist:
            maxDist = distance

print(math.ceil(maxDist / 2))