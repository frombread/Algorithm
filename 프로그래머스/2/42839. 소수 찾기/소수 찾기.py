from itertools import permutations

def solution(numbers):
    list = []
    for i in numbers:
        list.append(int(i));

    result_list = []
    for i in range(1,len(list)+1):
        for j in permutations(list,i):
            num=''
            for z in j:
                num += str(z);
            result_list.append(int(num))
    result_list = set(result_list)
    result= 0
    for i in result_list:
        if i>1:
            for j in range(2,i):
                if i % j==0:
                    break;
            else:
                result+=1
    return result;