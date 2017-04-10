import math

input()
temps = [int(i) for i in input().split()]  # the n temperatures expressed as integers ranging from -273 to 5526

if temps == []:
    print('0')
else:
    curMin = math.inf
    for i in temps:
        if abs(i) < abs(curMin):
            curMin = i
        elif abs(i) == abs(curMin):
            if i > curMin:
                curMin = i
    print(curMin)