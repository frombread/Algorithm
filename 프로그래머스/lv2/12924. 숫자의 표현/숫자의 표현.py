def solution(n):
    answer = 1
    a = []
    for i in range(1,n):
        a.append(i)
    for i in range(n,0,-1):
        woo =0
        woo +=i
        for j in range(i-1,0,-1):
            woo +=j
            if woo > n:
                break
            elif woo ==n:
                answer +=1
                break
            
    return answer