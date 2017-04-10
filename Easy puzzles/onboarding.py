while 1:
    e1 = input()  # name of enemy 1
    d1 = int(input())  # distance to enemy 1
    e2 = input()  # name of enemy 2
    d2 = int(input())  # distance to enemy 2

    if d1 < d2:
        print(e1)
    else:
        print(e2)