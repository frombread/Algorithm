def solution(brown, yellow):
    answer = [0,0]
    all = brown + yellow
    h,w =0,0
    for i in range(1,all+1):
        if all % i ==0:
            h = i
            w = all//i
            if (h-2) * (w-2) ==yellow:
                return [w,h]
        
    return answer