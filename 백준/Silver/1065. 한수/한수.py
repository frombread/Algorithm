import sys
num_1 = int(sys.stdin.readline())
count =0
for num_1 in range(1,num_1+1):
    b=list(map(int,str(num_1)))
    if num_1 <100:
        count+=1
    elif b[0]-b[1] == b[1]-b[2]:
        count +=1
print(count)
