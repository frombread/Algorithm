
def solution(number):
    answer = 0
    num_list =[]
    flag = [False]*len(number)
    for i in range(len(number)):
        combination(number,i,flag,0,"",num_list)
    for i in range(len(num_list)):
        a, b, c=map(int,num_list[i].split()) # "1 2 3"
        result=a+b+c
        if result == 0:
            answer += 1
    return answer

def combination(number,idx, flag, depth, str_, num_list):
    str_ = str_ + str(number[idx])
    flag[idx] = True
    if depth == 2:
        num_list.append(str_)
        return
    str_=str_+ " "
    for i in range(idx,len(number)):
          if flag[i] == False:
                combination(number,i,flag,depth+1,str_, num_list)
                flag[i] = False
        
        
