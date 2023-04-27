def fib(n):
    fib_list[0]=0
    fib_list[1]=1
    fib_list[2]=1
    if n <2:
        return fib_list[n]
    
    for i in range(2,n+2):
        fib_list[i]= fib_list[i-2]+fib_list[i-1]
    return fib_list[n]


n = int(input())
fib_list = [0 for _ in range(n+2)]
print(fib(n))