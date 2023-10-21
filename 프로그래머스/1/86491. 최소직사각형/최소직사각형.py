def solution(sizes):
    answer = 0
    r_max = 0
    l_max = 0
    for m in sizes:
        x,y = m
        if x < y:
            if r_max < y:
                r_max = y
            if l_max < x:
                l_max = x
        else:
            if r_max <x:
                r_max = x
            if l_max <y:
                l_max = y
    answer = l_max * r_max
    return answer