surface_n = int(input())
for i in range(surface_n):
    land_x, land_y = [int(j) for j in input().split()]

while True:
    turn = 0
    thrust = 0
    x, y, h_speed, v_speed, fuel, rotate, power = [int(i) for i in input().split()]
    s = land_y-y
    if v_speed < -39:
        thrust = 4
    elif v_speed > -37:
        thrust = 2
    else:
        thrust = 3
    print(turn, thrust)