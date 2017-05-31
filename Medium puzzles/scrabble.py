def evalScore(word):
    score = 0
    for i in word:
        if i in ['e', 'a,', 'i', 'o', 'n', 'r', 't', 'l', 's', 'u']:
            score += 1
        elif i in ['d', 'g']:
            score += 2
        elif i in ['b', 'c', 'm', 'p']:
            score += 3
        elif i in ['f', 'h', 'v', 'w', 'y']:
            score += 4
        elif i in ['k']:
            score += 5
        elif i in ['j', 'x']:
            score += 8
        elif i in ['q', 'z']:
            score += 10
    return score


n = int(input())
dictionary = []
for i in range(n):
    w = input()
    if len(w) <= 7:
        dictionary.append(w)
letters = sorted(input())

curHighestScore = -1
curWord = ''

for word in dictionary:
    w = sorted(word)
    for i in letters:
        if i in w:
            w.remove(i)
        else:
            continue

    if w == []:
        curScore = evalScore(word)
        if curScore > curHighestScore:
            curHighestScore = curScore
            curWord = word

print(curWord)