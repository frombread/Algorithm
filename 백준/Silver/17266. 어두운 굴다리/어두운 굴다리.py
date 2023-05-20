import sys
import math
input = sys.stdin.readline

m = int(input())
n = int(input())

street_lamp_list =list(map(int,input().split()))
# street_lamp_list.append(0)
# street_lamp_list.append(m)
street_lamp_list.sort()
result = []
for i in range(n-1):
    result.append(math.ceil(abs(street_lamp_list[i]-street_lamp_list[i+1])/2))

result.append(abs(street_lamp_list[-1]-m))
result.append(abs(0-street_lamp_list[0]))

print(max(result))
