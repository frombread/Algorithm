def solution(num_list):
    answer = 0
    a =[0,0] 
    for i in range(len(num_list)):
        if i%2 !=0:
            a[0] += num_list[i]
        else:
            a[1] += num_list[i]
            print(i)

                
    return max(a)