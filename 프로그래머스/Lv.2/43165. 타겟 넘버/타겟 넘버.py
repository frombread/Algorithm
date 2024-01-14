def solution(numbers, target):
    answer = 0
    list_ = []
    def dfs(depth,num):
        if depth == len(numbers):
            if num == target:
                list_.append(num)
            return
        dfs(depth+1,num+numbers[depth])
        dfs(depth+1,num-numbers[depth])
    dfs(0,0)
    return len(list_)