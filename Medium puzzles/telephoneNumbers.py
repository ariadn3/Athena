class node(object):
    number = None
    childTree = None

    def __init__(self):
        self.childTree = [None] * 10

    def insert(self, inNum):
        if inNum == '':
            return True
        firstNumber = int(inNum[0])
        restOfNumber = inNum[1:]

        if self.childTree[firstNumber] is None:
            self.childTree[firstNumber] = node()
        self.childTree[firstNumber].insert(restOfNumber)

    def getCount(self):
        sum = 1
        for n in self.childTree:
            if n is not None:
                sum += n.getCount()
        return sum

parentNode = node()

n = int(input())
for i in range(n):
    parentNode.insert(input())

print(parentNode.getCount() - 1)