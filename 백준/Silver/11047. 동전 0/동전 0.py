N,K = map(int,input().split())
coin_list =[]

for _ in range(N):
    coin_list.append(int(input()))

coin_list.sort()
coin_list.reverse()
count=0
for coin in coin_list:
    count += K//coin
    K = K%coin
print(count)

