def sum(num):
    if num ==1:
        return 1
    elif num ==2:
        return 2
    elif num ==3:
        return 4
    else: 
        return sum(num-3)+ sum(num-2) + sum(num-1)


n =int(input())
for _ in range(n):
    a=int(input())
    print(sum(a))