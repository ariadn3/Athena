import math
ulong,ulat = math.radians(float(input().replace(',','.'))),math.radians(float(input().replace(',','.')))
n = int(input())
curDistance = math.inf
curName = ''
for i in range(n):
    defib = input().replace(',','.').split(';')
    dlong = math.radians(float(defib[4]))
    dlat = math.radians(float(defib[5]))
    x = (dlong - ulong) * math.cos((dlat + ulat)/2)
    y = dlat - ulat
    d = math.sqrt(x**2 + y**2)*6371
    if d < curDistance:
        curDistance = d
        curName = defib[1]
print(curName)