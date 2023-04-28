n,k =map(int,input().split())

backpack = []

for _ in range(n):
    backpack.append(list(map(int,input().split())))

dp = [0]*(k+1)

for i in backpack:
    weight ,value =i
    for j in range(k,weight-1,-1):
        dp[j] = max(dp[j], dp[j-weight]+value)


print(dp[-1])