valueDict = {str(i):i for i in range(2,11)}
valueDict.update({'J':11, 'Q':12, 'K':13, 'A':14})

n = int(input())
p1Deck = [input()[:-1] for i in range(n)]
m = int(input())
p2Deck = [input()[:-1] for i in range(m)]

gameLength = 0
gameIndex = 0
while True:
    if not p1Deck[gameIndex:]:
        print(2, gameLength)
        break
    elif not p2Deck[gameIndex:]:
        print(1, gameLength)
        break
    else:
        gameLength += 1
        matchResult = valueDict[p1Deck[gameIndex]] - valueDict[p2Deck[gameIndex]]
        if matchResult > 0:
            p1Deck[len(p1Deck):] = p1Deck[0:gameIndex+1]
            p1Deck[len(p1Deck)+gameIndex:] = p2Deck[0:gameIndex+1]
            p1Deck = p1Deck[gameIndex+1:]
            p2Deck = p2Deck[gameIndex+1:]
            gameIndex = 0
        elif matchResult < 0:
            p2Deck[len(p2Deck):] = p1Deck[0:gameIndex+1]
            p2Deck[len(p2Deck)+gameIndex:] = p2Deck[0:gameIndex+1]
            p1Deck = p1Deck[gameIndex+1:]
            p2Deck = p2Deck[gameIndex+1:]
            gameIndex = 0
        else:
            if len(p1Deck) < gameIndex+4 or len(p2Deck) < gameIndex+4:
                print('PAT')
                break
            else:
                gameIndex += 4
                gameLength -= 1