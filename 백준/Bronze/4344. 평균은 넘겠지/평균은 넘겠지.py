import sys
fir=int(sys.stdin.readline())

for _ in range(fir):
    lis=list(map(int,sys.stdin.readline().split()))
    b =lis[1:]
    c=[]
    avg=sum(b)/len(b)
    for i in b:
        if i > avg:
            c.append(i)
        else:
            pass
    print(f"{round(len(c)/len(b)*100,3):.3f}%")
