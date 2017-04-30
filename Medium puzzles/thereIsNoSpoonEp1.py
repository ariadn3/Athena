width = int(input())
height = int(input())

nodeMap, nodeList = [], []
rightDict, btmDict = {}, {}

for i in range(height):
    line = input()
    nodeMap.append(line)
    prevXNode = -1
    for j in range(width):
        if line[j] == '0':
            nodeList.append((j, i))
            if prevXNode != -1:
                rightDict[prevXNode, i] = (j, i)
            prevXNode = j

for i in range(width):
    prevYNode = -1
    for j in range(height):
        if nodeMap[j][i] == '0':
            if prevYNode != -1:
                btmDict[i, prevYNode] = (i, j)
            prevYNode = j

for node in nodeList:
    x, y = node
    right, rightY = -1, -1
    btm, btmX = -1, -1

    try:
        right, rightY = rightDict[x, y]
    except KeyError:
        pass
    try:
        btmX, btm = btmDict[x, y]
    except KeyError:
        pass

    print("{} {} {} {} {} {}".format(x, y, right, rightY, btmX, btm))