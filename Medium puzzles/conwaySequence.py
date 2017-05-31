class conwayList(object):
    conwaySeq = None

    def __init__(self, firstValue):
        self.conwaySeq = [firstValue]

    def mutate(self):
        nextSeq = []
        count, num = -1, -1
        for i in self.conwaySeq:
            if num != i:
                if num != -1:
                    nextSeq.append(count)
                    nextSeq.append(num)
                num = i
                count = 1
            else:
                count += 1
        nextSeq.append(count)
        nextSeq.append(num)
        self.conwaySeq = nextSeq

    def getConwaySeq(self):
        result = ''
        for i in self.conwaySeq:
            result += str(i) + ' '
        result = result[:-1]
        return result


r = int(input())
l = int(input()) - 1

initSeq = conwayList(r)
for i in range(l):
    initSeq.mutate()
print(initSeq.getConwaySeq())
