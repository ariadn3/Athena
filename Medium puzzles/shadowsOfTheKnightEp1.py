w, h = [int(i) for i in input().split()]
int(input())
x, y = [int(i) for i in input().split()]

xLower, xUpper = 0, w
yLower, yUpper = 0, h

while True:
    dir = input()  # the direction of the bombs from batman's current location (U, UR, R, DR, D, DL, L or UL)
    if 'U' in dir:
        yUpper = y - 1
    elif 'D' in dir:
        yLower = y + 1
    else:
        yLower = yUpper = y

    if 'R' in dir:
        xLower = x + 1
    elif 'L' in dir:
        xUpper = x - 1
    else:
        xLower = xUpper = x

    x = (xLower + xUpper) // 2
    y = (yLower + yUpper) // 2

    print(x, y)