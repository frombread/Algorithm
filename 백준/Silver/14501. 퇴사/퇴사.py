import sys

input = sys.stdin.readline

N = int(input())
num_list = [[0,0]]
dp = [0]*(N+2)

for _ in range(N):
    a, b = map(int, input().split())
    num_list.append([a,b])
    
for i in range(N, 0, -1):
    if i + num_list[i][0] <= N + 1:
        dp[i] = max(dp[i + num_list[i][0]] + num_list[i][1], dp[i + 1])
    else:
        dp[i] = dp[i + 1]

print(dp[1])
