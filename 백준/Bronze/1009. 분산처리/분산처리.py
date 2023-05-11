import sys
input = sys.stdin.readline

T= int(input())
for _ in range(T):
    a,b = map(int, input().split())

    a %= 10
    b =b%4 + 4
    result  = a**b%10
    if result == 0:
        print(10)
    else:
        print(result)