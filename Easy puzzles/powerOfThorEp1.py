lx, ly, ix, iy = [int(i) for i in input().split()]
while True:
    direction = ''
    if iy>ly:
        direction+='N'
        iy-=1
    elif iy<ly:
        direction+='S'
        iy+=1
    if ix>lx:
        direction+='W'
        ix-=1
    elif ix<lx:
        direction+='E'
        ix+=1
    print(direction)