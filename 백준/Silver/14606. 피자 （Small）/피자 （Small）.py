import sys
iiput = sys.stdin.readline

N= int(input())
dp =[0] * 11
dp[1]=0
dp[2]=1

for pizza in range(N+1):
    pizza_half=pizza//2
    mod=pizza-pizza_half
    dp[pizza] = dp[pizza_half] + dp[mod] + (pizza_half * mod)

print(dp[N])