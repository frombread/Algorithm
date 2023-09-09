def solution(left, right):
    answer = 0
    for i in range(left , right+1):
        a = get_divisor(i)
        if a % 2==0:
            answer +=i
        else:
            answer -= i
    return answer

def get_divisor(n):
    data = []

    for i in range(1, n // 2 + 1):
        if n % i == 0:
            data.append(i)
    data.append(n)
    return len(data)