import sys
lis=[]
for _ in range(9):
    lis.append(int(input()))
    

sum_ = sum(lis)


for i in range(len(lis)):
    for j in range(1,len(lis)):
        if sum_- lis[i]-lis[j] == 100:
            No_num_1,No_num_2 = lis[i],lis[j]
            break

lis.sort()
for r in lis:
    if r != No_num_1 and r!=No_num_2:
        print(r)
