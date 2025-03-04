n = int(input())
n_list = list(map(int,input().split()))
dp=[0 for _ in range(n)]
dp[0]=n_list[0]
for i in range(1,n):
    for j in range(i):
        if n_list[i] > n_list[j]:
            dp[i] = max(dp[i],dp[j]+n_list[i])
        else:
            dp[i] = max(dp[i],n_list[i])

print(max(dp))
