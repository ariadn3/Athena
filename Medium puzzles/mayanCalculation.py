import operator

# Generating dictionary
l, h = [int(i) for i in input().split()]
numeralList = ['' for i in range(20)]
for i in range(h):
    numeralRaw = input()
    for j in range(20):
        numeralList[j] += (numeralRaw[j*l:(j+1)*l]) + '\n'
numeralDict = {}
for i in range(20):
    numeralDict.update({numeralList[i]: i})

s1 = int(input())
n1 = 0
for i in range(s1//h):
    block = ''
    n1 *= 20
    for j in range(h):
        block += input() + '\n'
    n1 += numeralDict[block]

s2 = int(input())
n2 = 0
for i in range(s2//h):
    block = ''
    n2 *= 20
    for j in range(h):
        block += input() + '\n'
    n2 += numeralDict[block]

operation = input()
operatorLookup = {'+': operator.add,
                  '-': operator.sub,
                  '*': operator.mul,
                  '/': operator.floordiv}

answer = operatorLookup[operation](n1, n2)
if answer == 0:
    print(numeralList[0])
    exit()
answerString = ''

while answer!= 0:
    rem = answer%20
    answer //= 20
    answerString = numeralList[rem] + answerString

print(answerString)