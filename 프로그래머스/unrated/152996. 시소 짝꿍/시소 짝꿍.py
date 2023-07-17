from collections import defaultdict

def solution(weights):
    answer = 0
    weight_dict =defaultdict(int)

    for weight in weights :
        weight_dict[weight] += 1

    for i,j in weight_dict.items():
        if j > 1:
            answer += j*(j-1)//2
        if i*2 in weight_dict:
            answer += j * weight_dict[i * 2]
            # print(j * weight_dict[i * 2])
        if i * 3 % 2 == 0 and i*3 // 2  in weight_dict:
            answer += j * weight_dict[i * 3//2]
            # print(j * weight_dict[i *3//2])
        if i*4 % 3 == 0 and i*4 // 3 in weight_dict :
            answer += j * weight_dict[i * 4//3]
            # print(j * weight_dict[i * (4//3)])


    return answer