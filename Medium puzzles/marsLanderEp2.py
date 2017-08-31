import sys

surface_n = int(input())  # the number of points used to draw the surface of Mars.
surfaceNodeList = []
flatSurface = (-1, -1)
for i in range(surface_n):
    # land_x: X coordinate of a surface point. (0 to 6999)
    # land_y: Y coordinate of a surface point. By linking all the points together in a sequential fashion, you form the surface of Mars.
    land_x, land_y = [int(j) for j in input().split()]
    if len(surfaceNodeList) == 0:
        surfaceNodeList.append((land_x, land_y))
        continue
    if land_y == surfaceNodeList[len(surfaceNodeList)-1][1]:
        flatSurface = (surfaceNodeList[len(surfaceNodeList)-1][0], land_x)
    surfaceNodeList.append((land_x, land_y))
print(flatSurface, file=sys.stderr)
# game loop
while True:
    # h_speed: the horizontal speed (in m/s), can be negative.
    # v_speed: the vertical speed (in m/s), can be negative.
    # fuel: the quantity of remaining fuel in liters.
    # rotate: the rotation angle in degrees (-90 to 90).
    # power: the thrust power (0 to 4).
    x, y, h_speed, v_speed, fuel, rotate, power = [int(i) for i in input().split()]

    if x < flatSurface[0]:
        if h_speed < 50:
            rotate = -45
            power = 4
        elif h_speed > 50:
            rotate = 25
            power = 4
        else:
            rotate = 0
            power = 4
    elif x > flatSurface[1]:
        if h_speed > -50:
            rotate = 45
            power = 4
        elif h_speed < -50:
            rotate = -25
            power = 4
        else:
            rotate = 0
            power = 4
        if v_speed > 4:
            power = 0
    else:
        if h_speed > 50:
            rotate = 45
            power = 4
        elif 50 >= h_speed > 10:
            rotate = 30
            power = 4
        elif 10 >= h_speed > 0:
            rotate = 22
            power = 4
        elif 0 > h_speed >= -10:
            rotate = -22
            power = 4
        elif -10 > h_speed >= -50:
            rotate = -30
            power = 4
        elif -50 > h_speed:
            rotate = -45
            power = 4
        elif h_speed < 0:
            rotate = -30
            power = 4
        else:
            rotate = 0
            if v_speed < -35:
                power = 4
            else:
                power = 0
    print('{} {}'.format(rotate, power))
