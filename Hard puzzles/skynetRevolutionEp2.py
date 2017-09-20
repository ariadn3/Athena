n, l, e = [int(i) for i in input().split()]
adjDict = {i:set() for i in range(n)}

for i in range(l):
    n1, n2 = [int(j) for j in input().split()]
    adjDict[n1].add(n2)
    adjDict[n2].add(n1)

gatewaySet = set()
for i in range(e):
    gatewaySet.add(int(input()))

while True:
    visitedSet = set()
    severList = []
    nodeList = [(int(input()), 0, 0)]
    while True:
        if not nodeList:
            break
        node, dist, heuristic = nodeList.pop(0)
        if node in visitedSet:
            continue

        for i in adjDict[node]:
            if i in gatewaySet:
                heuristic -= 1
                severList.append((heuristic, dist, node, i))

        for i in adjDict[node]:
            if i not in gatewaySet:
                nodeList.append((i, dist+1, heuristic+1))
        visitedSet.add(node)
    severList = sorted(severList, key = lambda x: x[0:2])
    print(severList, file = sys.stderr)
    node1, node2 = severList[0][2:4]
    print(str(node1) + ' ' + str(node2))
    adjDict[node1].remove(node2)
    adjDict[node2].remove(node1)