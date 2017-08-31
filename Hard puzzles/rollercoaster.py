slots, times, n = [int(i) for i in input().split()]
groupList = []
for i in range(n):
    groupList.append(int(input()))

if sum(groupList) <= slots:
    print(str(sum(groupList) * times))
    exit(0)

earnings, seats, counter = 0, 0, 0
size = len(groupList)
startIndex = 0
endIndex = [-1]*size

for i in range(times):
    if endIndex[counter%size] != -1:
        earnings += endIndex[counter%size][1]
        startIndex = counter = endIndex[counter%size][0]
        continue
    while True:
        j = groupList[counter%size]
        if j + seats <= slots:
            seats += j
            counter += 1
        else:
            endIndex[startIndex] = (counter%size, seats)
            earnings += seats
            seats = 0
            startIndex = counter%size
            break

print(earnings)