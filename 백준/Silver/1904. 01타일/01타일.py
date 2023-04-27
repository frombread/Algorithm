def fib(n):
    fib_list[0]=1
    fib_list[1]=1
    
    for i in range(2,n+2):
        fib_list[i]= (fib_list[i-2]+fib_list[i-1]) % 15746
    return fib_list[n]

n = int(input())
fib_list =[0 for _ in range(n+2)]
print(fib(n))
