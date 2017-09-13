import copy

l = int(input())
h = int(input())

isWater = [[0] * l for i in range(h)]
depth = copy.deepcopy(isWater)
checkedList = []

for i in range(h):
    row = input()
    for j in range(l):
        if row[j] == 'O':
            isWater[i][j] = True

checkingList = []
def checkWater():
    for coords in checkingList:
        x, y, t = coords
        if x < 0 or x > l - 1 or y < 0 or y > h - 1 or not isWater[y][x]:
            continue

        isWater[y][x] = False
        checkedList.append((x, y))
        if t != 1:
            checkingList.append((x + 1, y, 2))
        if t != 2:
            checkingList.append((x - 1, y, 1))
        if t != 3:
            checkingList.append((x, y + 1, 4))
        if t != 4:
            checkingList.append((x, y - 1, 3))

n = int(input())
for i in range(n):
    x, y = [int(j) for j in input().split()]
    if not isWater[y][x]:
        print(depth[y][x])
        continue

    checkingList.append((x, y, 0))
    checkWater()

    d = len(checkedList)
    for j in checkedList:
        depth[j[1]][j[0]] = d
    checkedList = []
    checkingList = []
    print(d)
