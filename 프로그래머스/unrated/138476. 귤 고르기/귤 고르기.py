# def solution(k, tangerine):
#     res =[]
#     a= set(tangerine)
#     for i in a:
#         res.append(tangerine.count(i))
#     res.sort()
#     answer = 0
#     s= 0
#     while (s < k):
#         s += res.pop()
#     return answer
def solution(k, tangerine):
    res =[0]*(10000001)
    for i in tangerine:
        if res[i] is None:
            res[i] = 1
        else:
            res[i] = res[i] + 1
    res.sort()
    answer = 0
    s= 0
    while (s < k):
        s += res.pop()
        answer +=1
    return answer

    
    