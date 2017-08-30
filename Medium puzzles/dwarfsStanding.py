import sys

visitedList = []
toVisit = 0
nodeList = []

n = int(input())  # the number of relationships of influence
neighbourDict = {}
for i in range(n):
    # x: a relationship of influence between two people (x influences y)
    x, y = [int(j) for j in input().split()]
    if x not in nodeList:
        nodeList.append(x)
    if y not in nodeList:
        nodeList.append(y)

    try:
        neighbourDict[x].append(y)
    except KeyError:
        neighbourDict[x] = [y]

def visitRecur(path, curNode):
    #print('Currently trying: ' + str(path) + ' @' + str(curNode), file=sys.stderr)
    minLength = 0
    try:
        for i in neighbourDict[curNode]:
            newPath = path + [curNode]
            pathLength = visitRecur(newPath, i)
            if minLength < pathLength:
                minLength = pathLength
        return minLength
    except:
        #print('End node reached: ' + str(path + [curNode]), file=sys.stderr)
        return len(path) + 1


minTotal = 0
for i in nodeList:
    length = visitRecur([], i)
    if minTotal < length:
        minTotal = length

print(minTotal)