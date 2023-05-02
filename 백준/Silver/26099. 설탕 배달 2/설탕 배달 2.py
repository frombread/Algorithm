import sys

input= sys.stdin.readline

K = int(input())

count =0
while True:
    if K%5 != 0:
        K=K-3
        count+=1
    else:
        count += K//5
        print(count)
        break
        
    if K<0:
        print(-1)
        break
