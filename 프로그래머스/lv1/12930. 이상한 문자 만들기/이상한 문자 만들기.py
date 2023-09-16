def solution(s):
    answer_list = []
    text_list = s.split(' ')
    for text in text_list:
        string_list=[]
        for i in range(len(text)):
            if i%2==0:
                string_list.append(text[i].upper())
            else:
                string_list.append(text[i].lower())
        answer_list.append(''.join(string_list))
    answer = ' '.join(answer_list)
    
    return answer
