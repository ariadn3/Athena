dirTransDict = {'S': 'SOUTH', 'E': 'EAST', 'N': 'NORTH', 'W': 'WEST'}
dirValueDict = {'S': (0, 1), 'E': (1, 0), 'N': (0, -1), 'W': (-1, 0)}

dirPriority = ['S', 'E', 'N', 'W']
curDir = 'S'
curPos = (-1, -1)
endPos = (-1, -1)
curBreaker = False

dirHistory = set()
completeDirHistory = []
teleList = []
map = []

l, c = [int(i) for i in input().split()]
for y in range(l):
    row = input()
    map.append(list(row))
    for x in range(c):
        if row[x] == '@':
            curPos = (x, y)
        elif row[x] == '$':
            endPos = (x, y)
        elif row[x] == 'T':
            teleList.append((x, y))

# for i in map:
#    for j in i:
#        print(j, file=sys.stderr, end = '')
#    print(file=sys.stderr)
# print(file=sys.stderr)

while curPos != endPos:
    # Check if in loop
    if (curPos, curDir, curBreaker) in dirHistory:
        print('LOOP')
        quit()

    # Resolve future direction
    cx, cy = curPos
    fx = dirValueDict[curDir][0]
    fy = dirValueDict[curDir][1]
    tile = map[cy + fy][cx + fx]
    if tile == '#' or (tile == 'X' and not curBreaker):
        for i in dirPriority:
            curDir = i
            fx = dirValueDict[curDir][0]
            fy = dirValueDict[curDir][1]
            tile = map[cy + fy][cx + fx]
            if tile == '#' or (tile == 'X' and not curBreaker):
                continue
            else:
                break
    if tile == 'X' and curBreaker:
        map[cy + fy][cx + fx] = ' '
        dirHistory = set()
    # print('{},{} heading {}'.format(cx, cy, curDir), file=sys.stderr)

    # Resolve movement
    dirHistory.add((curPos, curDir, curBreaker))
    curPos = (cx + fx, cy + fy)
    completeDirHistory.append(curDir)

    # Resolve tile action
    if tile == 'S':
        curDir = 'S'
    elif tile == 'E':
        curDir = 'E'
    elif tile == 'N':
        curDir = 'N'
    elif tile == 'W':
        curDir = 'W'
    elif tile == 'I':
        dirPriority = dirPriority[::-1]
    elif tile == 'B':
        curBreaker = not curBreaker
    elif tile == 'T':
        if curPos == teleList[0]:
            curPos = teleList[1]
        else:
            curPos = teleList[0]

# print(file=sys.stderr)
for d in completeDirHistory:
    print(dirTransDict[d])