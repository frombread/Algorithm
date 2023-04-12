import sys

n, r, c = map(int, sys.stdin.readline().split())


def coordinate(n, r, c):
    mid_num = 2**(n-1)
    if n == 1:
        if (r < 1) and (c < 1):
            return 0
        elif (r < 1) and (c >= 1):
            return 1
        elif (r >= 1) and (c < 1):
            return 2
        elif (r >= 1) and (c >= 1):
            return 3
    elif n > 1:
        if (r < mid_num) and (c < mid_num):
            return coordinate(n-1, r, c)
        elif (r < mid_num) and (c >= mid_num):
            return coordinate(n-1, r, c-2**(n-1)) + 2**(2*(n-1))*1
        elif (r >= mid_num) and (c < mid_num):
            return coordinate(n-1, r-2**(n-1), c) + 2**(2*(n-1))*2
        elif (r >= mid_num) and (c >= mid_num):
            return coordinate(n-1, r-2**(n-1), c-2**(n-1)) + 2**(2*(n-1))*3


print(coordinate(n, r, c))