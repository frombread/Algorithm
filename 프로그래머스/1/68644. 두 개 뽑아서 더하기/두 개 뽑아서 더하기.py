def solution(numbers):
    answer = []
    new =[]
    flag = [False] * (len(numbers)+1)
    
    def dfs(idx):
        nonlocal new
        if len(new)==2:
            answer.append(new.copy())
            return
        
        for i in range(len(numbers)):
            if flag[i] ==False:
                new.append(numbers[i])
                flag[i] =True
                dfs(i)
                flag[i] =False
                new.pop()
    dfs(0)
    result =[]
    for i in answer:
        x,y = i
        result.append(x+y)
    answer = list(set(result))
    answer.sort()
    return answer

