n = int(input())
c = int(input())
budgetList = []
for i in range(n):
    b = int(input())
    budgetList.append(b)

if sum(budgetList) < c:
    print('IMPOSSIBLE')
    exit()

budgetList.sort()

counter = 0

while budgetList[0] == counter:
    print(budgetList[0])
    budgetList = budgetList[1:]

while c > 0:
    oodsLeft = len(budgetList)
    # print('Turn {}: {} left -- {} remaining'.format(counter, c, budgetList), file = sys.stderr)

    if oodsLeft < c:
        counter += 1
        c -= oodsLeft
        while budgetList[0] == counter:
            print(budgetList[0])
            budgetList = budgetList[1:]
        continue
    else:
        totalPeople = oodsLeft
        for i in range(totalPeople - c):
            print(counter)
        counter += 1
        for i in range(c):
            print(counter)
        exit()
