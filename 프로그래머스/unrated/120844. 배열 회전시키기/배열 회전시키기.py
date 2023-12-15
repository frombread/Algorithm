def solution(numbers, direction):
    answer = [0] *len(numbers)
    if direction == "right":
        answer[0] = numbers[len(numbers)-1]
        for i in range(1,len(numbers)):
            answer[i] = numbers[i-1]
    else:
        answer[len(numbers)-1] = numbers[0]
        for i in range(len(numbers)-1):
            answer[i] =numbers[i+1]

    print(answer)
    return answer