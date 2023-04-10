import sys
x, y = map(int,sys.stdin.readline().split())
z = list(map(int,sys.stdin.readline().split()))

for i in list(z):
    if int(i) < y:
        print(i)
    else:
        pass