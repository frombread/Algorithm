import sys
input = sys.stdin.readline
n = int(input())
max_value,min_value=-999999999,999999999

def dfs(idx, num):
    global a,b,c,d,max_value,min_value
    if idx ==n:
        max_value = max(max_value,num)
        min_value = min(min_value,num)
    else:
        if a>0:
            a-=1
            dfs(idx+1,num+num_list[idx])
            a+=1
        if b>0:
            b-=1
            dfs(idx+1, num-num_list[idx])
            b+=1
        if c>0:
            c-=1
            dfs(idx+1,num*num_list[idx])
            c+=1
        if d>0:
            d-=1
            dfs(idx+1,int(num/num_list[idx]))
            d+=1


num_list= list(map(int,input().split()))
a,b,c,d = map(int, input().split())

result =[]
dfs(1,num_list[0])

print(max_value)
print(min_value)
