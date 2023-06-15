def solution(name, yearning, photo):
    answer = []
    dic=[]
    for i,j in zip(name,yearning):
        dic.append([i,j])
    
    for photoes in photo:
        ans =0
        for per in photoes:
            for i in dic:            
                if per == i[0]:
                    ans+=i[1]
        answer.append(ans)
    return answer