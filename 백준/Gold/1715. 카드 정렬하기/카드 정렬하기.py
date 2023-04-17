import heapq
import sys
n=int(sys.stdin.readline())
card=[]
for _ in range(n):
    heapq.heappush(card,int(sys.stdin.readline()))

sum=0
while len(card) >1:
    fir_card = heapq.heappop(card)
    sec_card = heapq.heappop(card)
    temp =fir_card+sec_card
    sum +=temp
    heapq.heappush(card,temp)

print(sum)