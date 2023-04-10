import sys
x, y = map(int, sys.stdin.readline().split())

x_ori= [0,x]
y_ori= [0,y]
for i in range(int(sys.stdin.readline())):
    a, b = map(int, sys.stdin.readline().split())
    if a ==0:
        y_ori.append(b)
    else:
        x_ori.append(b)
y_ori.sort()
x_ori.sort()
max_h=0
for i in range(1,len(x_ori)):
    for j in range(1,len(y_ori)):
        x_o = x_ori[i]-x_ori[i-1]
        y_o = y_ori[j]-y_ori[j-1]
        max_h= max(max_h,x_o*y_o)

print(max_h)