import sys

x=int(sys.stdin.readline())
count=0
test_number = list(map(int, sys.stdin.readline().split()))

for b in test_number:
    for i in range(2,b+1):
        if b % i ==0:
            if b==i:
                count+=1
            break
            
print(count)
        