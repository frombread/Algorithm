from collections import deque
def solution(s):
    list_s= deque()
    for i in s:
        list_s.append(i)
    list1= []
    for _ in range(1,len(list_s)+1):
        a = list_s.popleft()
        if a =="(":
            list1.append(a)
        elif a ==")":
            if len(list1) == 0:
                return False
            list1.pop()
    if 0 < len(list1):
                return False
    return True