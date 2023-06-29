n= int(input())
m=n
while m!=1:
    for i in range(2,n+1):
        if m%i == 0:
            print(i)
            m = m/i
            break

