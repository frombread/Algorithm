import sys
input = sys.stdin.readline

N= int(input())
num_list =[]
for _ in range(N):
    num_list.append(list(map(int,input().split())))

dp = [[0] * (N) for _ in range(N)]
dp[0][0]=1
for row in range(N):
    for col in range(N):
        next_x = row+num_list[row][col]
        next_y = col+num_list[row][col]

        if num_list[row][col] == 0 :
            break
        if next_x<N:
            dp[next_x][col] += dp[row][col]
        if next_y<N:
            dp[row][next_y] += dp[row][col]


print(dp[-1][-1])

