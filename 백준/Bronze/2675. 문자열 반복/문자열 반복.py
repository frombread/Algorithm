import sys
a= int(sys.stdin.readline())
for i in range(a):
    x,y=map(str,sys.stdin.readline().split())
    m=[]
    for p in y:
        m += int(x)*p

    print("".join(m))