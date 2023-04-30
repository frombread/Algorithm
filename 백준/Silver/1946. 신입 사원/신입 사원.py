import sys
input = sys.stdin.readline
T = int(input())

for _ in range(T):
    resume =[]
    n = int(input())
    count =1
    for i in range(n):
        resume.append(list(map(int,input().split())))
    resume.sort()    
    d = resume[0][1]
    for fir, sec in resume:
        if sec < d:
            count+=1
            d = sec
    print(count)
    