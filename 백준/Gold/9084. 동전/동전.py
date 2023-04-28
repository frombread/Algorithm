T = int(input())
for _ in range(T):
    n= int(input())
    coin_list = map(int,input().split())
    m=int(input())
    dp =[1]+ [0]*m
    for coin in coin_list:
        for i in range(1,m+1):
            if i>=coin:
                dp[i]+=dp[i-coin]

    print(dp[m])
