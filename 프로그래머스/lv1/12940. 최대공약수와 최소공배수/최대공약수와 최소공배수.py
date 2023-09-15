import math
def solution(n, m):
    answer = [0,0]
    answer[0] = math.gcd(n,m)
    answer[1]=(n*m)/answer[0]
    return answer