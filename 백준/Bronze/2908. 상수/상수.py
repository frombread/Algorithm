import sys

x, y=map(str,sys.stdin.readline().split())

fir=int(x[2]+x[1]+x[0])
sec=int(y[2]+y[1]+y[0])
print(max(fir,sec))