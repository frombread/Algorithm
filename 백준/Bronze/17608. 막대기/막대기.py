import sys

a= int(sys.stdin.readline())
stk_list =[]
count= 0
max = 0
for _ in range(a):
    stk_list.append(int(sys.stdin.readline()))

for i in reversed(stk_list):
    if max < i:
        max =i 
        count +=1
    
print(count)