def solution(book_time):
    book_list=[]
    for i in book_time:
        book_list.append([int(i[0][0:2])*60+int(i[0][3:5]),int(i[1][0:2])*60+int(i[1][3:5])])
    book_list.sort(key = lambda x : (x[1],x[0]))
    answer = 0
    max_answer = 0
    for i in range(1440):
        for s, e in book_list:
            if e + 10 == i:
                answer -=1
        for s, e in book_list:
            if s == i:
                answer +=1
        if(answer > max_answer):
            max_answer = answer
        
    return max_answer