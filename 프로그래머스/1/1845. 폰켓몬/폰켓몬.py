def solution(nums):
    dic={}
    
    for i in range(len(nums)):
        dic[nums[i]]=i
    if len(dic) < len(nums)/2:
        return len(dic)
    
    return len(nums)/2