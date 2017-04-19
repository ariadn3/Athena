import sys

f, w, nb_r, exitf, exitp, nb_tc, nb_ae, nb_e = [int(i) for i in input().split()]

floorList = []
for i in range(nb_e):
    floorList.append([int(i) for i in input().split()])
floorList.sort()
floorList.append([exitf, exitp])

# first game loop + logic
cf, cp, dir = input().split()
floorList.insert(0, [int(cf), int(cp)])
decisionList = []
right = True
for i in range(1, len(floorList)):
    curPos = floorList[i - 1][1]
    nextPos = floorList[i][1]
    if (nextPos < curPos and right) or (nextPos > curPos and not right):
        decisionList.append(floorList[i][0])
        right = not right
if cf in decisionList:
    print("BLOCK")
    decisionList.remove(cf)
else:
    print("WAIT")

# game loop
while True:
    cf, cp, dir = input().split()
    cf = int(cf)
    cp = int(cp)
    if cf in decisionList:
        print("BLOCK")
        decisionList.remove(cf)
    else:
        print("WAIT")