import sys

def result(gridType, entry):
    if gridType == 1:
        return ((0,1), 'TOP')
    elif gridType == 2 or gridType == 6:
        if entry == 'LEFT':
            return ((1,0), 'LEFT')
        elif entry == 'RIGHT':
            return ((-1,0), 'RIGHT')
    elif gridType == 3:
        if entry == 'TOP':
            return ((0,1), 'TOP')
    elif gridType == 4:
        if entry == 'TOP':
            return ((-1,0), 'RIGHT')
        elif entry == 'RIGHT':
            return ((0,1), 'TOP')
    elif gridType == 5:
        if entry == 'TOP':
            return ((1,0), 'LEFT')
        elif entry == 'LEFT':
            return ((0,1), 'TOP')
    elif gridType == 7:
        if entry == 'LEFT':
            return -1
        else:
            return ((0,1), 'TOP')
    elif gridType == 8:
        if entry == 'TOP':
            return -1
        else:
            return ((0,1), 'TOP')
    elif gridType == 9:
        if entry == 'RIGHT':
            return -1
        else:
            return ((0,1), 'TOP')
    elif gridType == 10 and entry == 'TOP':
            return ((-1,0), 'LEFT')
    elif gridType == 11 and entry == 'TOP':
            return ((1,0), 'LEFT')
    elif gridType == 12 and entry == 'RIGHT':
            return ((0,1), 'TOP')
    elif gridType == 13 and entry == 'LEFT':
            return ((0,1), 'TOP')
    return -1

w, h = [int(i) for i in input().split()]
grid = []
for i in range(h):
    grid.append([int(i) for i in input().split()])
ex = int(input())

# turn = 0
while True:
    # turn += 1
    xi, yi, pos = input().split()
    xi = int(xi)
    yi = int(yi)
    # print('Turn ' + str(turn) + ': ' + str(xi) + ', ' + str(yi), file=sys.stderr)
    resPos = result(grid[yi][xi], pos)[0]
    xi += resPos[0]
    yi += resPos[1]
    print(str(xi) + ' ' + str(yi))