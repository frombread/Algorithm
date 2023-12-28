def solution(binomial):
    answer = 0
    list_ = ["*","+","-"]
    num_str =""
    str_ = ""
    for i in binomial:
        if i in list_:
            num_=int(num_str)
            num_str =" "
            str_ +=i
        else:
            num_str += i
    
    if str_ == "+":
        answer = num_ + int(num_str)
    elif str_=="*":
        answer = num_ * int(num_str)
    else:
        answer = num_ - int(num_str)
        
    return answer