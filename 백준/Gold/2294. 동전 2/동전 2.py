from collections import deque

q = deque()
q.append((0, 0))
n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]
visited = [False] * (k + 1)
visited[0] = True
result = -1
def bfs():
    global result
    while q:
        cost, cnt = q.popleft()

        for coin in coins:
            new_cost = cost + coin
            if new_cost <= k and not visited[new_cost]:
                visited[new_cost] = True
                q.append((new_cost, cnt + 1))
                if new_cost ==k:
                    result = cnt+1
bfs()
print(result)