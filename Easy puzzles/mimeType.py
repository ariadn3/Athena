n = int(input())
q = int(input())
mime = {}
for i in range(n):
    ext, mt = input().split()
    mime[ext.lower()] = mt
for i in range(q):
    raw = input()
    if '.' not in raw:
        print("UNKNOWN")
        continue
    fname = str.partition(raw.lower()[::-1],'.')[0][::-1]
    try:
        print(mime[fname])
    except:
        print("UNKNOWN")