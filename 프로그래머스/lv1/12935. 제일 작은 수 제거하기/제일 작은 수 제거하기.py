def solution(arr):
    if len(arr) ==1:
        arr[0]= -1
        return arr
    a=min(arr)
    arr.remove(a)
    return arr