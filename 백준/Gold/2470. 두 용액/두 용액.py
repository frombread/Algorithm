import sys

n =int(sys.stdin.readline())
num_list =list(map(int,sys.stdin.readline().split()))


num_list.sort()
final = []

left = 0
right = n-1

d= 1e10
while left<right:

    lv= num_list[left]
    rv= num_list[right]

    sum = lv+rv
    if abs(sum)<d:
        d=abs(sum)
        final=(lv,rv)
    if sum<0:
        left +=1
    else:
        right -=1

print(*final)