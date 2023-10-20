def solution(d, budget):
    d.sort()
    cnt =0
    print(d)
    for i in range(len(d)):
        budget -= d[i]
        if budget > 0:
            cnt +=1
        if budget < 0:
            break
        if budget == 0:
            cnt+=1

    return cnt