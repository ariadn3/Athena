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
    nodeList = [(int(input()), -1)]
    while True:
        node, prevNode = nodeList.pop(0)
        if node in visitedSet:
            continue
        elif node in gatewaySet:
            print(node, prevNode)
            adjDict[node].remove(prevNode)
            adjDict[prevNode].remove(node)
            break
        else:
            for i in adjDict[node]:
                nodeList.append((i, node))
            visitedSet.add(node)