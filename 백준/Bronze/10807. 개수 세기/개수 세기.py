n= int(input())
num_list = list(map(int,input().split()))
k = int(input())
cnt =0  
for i in num_list:
    if i == k:
        cnt +=1
    
print(cnt)