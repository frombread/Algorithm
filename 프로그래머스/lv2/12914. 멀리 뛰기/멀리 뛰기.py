def solution(n):
    answer = 0
    dp = [0] * (n+2)
    dp[1] = 1
    dp[2] = 1
    
    for i in range(3,n+2):
        dp[i] = dp[i-1]+dp[i-2]
    answer = (dp[n+1])%1234567
    return answer