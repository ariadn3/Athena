l = int(input())
h = int(input())
t = [ord(i)-97 for i in input().lower()]
row = [input() for i in range(h)]
for x in range(h):
    message = ''
    for i in t:
        if i < 0 or i > 25: # 97 to 122
            message += ''.join(row[x][26*l:27*l])
        else:
            message += ''.join(row[x][i*l:(i+1)*l])
    print(message)