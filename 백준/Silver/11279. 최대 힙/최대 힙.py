import heapq
import sys
first_input=int(sys.stdin.readline())

max_heap =[]
for _ in range(first_input):
    in_input = int(sys.stdin.readline())
    
    if in_input == 0:
        if len(max_heap) ==0:
            max_item = 0
        else:
            max_item = heapq.heappop(max_heap)[1]
        print(max_item)
    else:
         heapq.heappush(max_heap,(-in_input,in_input))
          