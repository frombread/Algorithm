def solution(hp):
    answer = 0
    ants =[5,3,1]
    for i in ants:
        while True:
            hp -=i
            if hp < 0:
                hp = hp + i
                break
            elif hp == 0:
                answer+=1                
                break
            answer+=1
            
    return answer