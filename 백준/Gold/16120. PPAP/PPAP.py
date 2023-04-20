n = list(input())

stk_list =[]

if 1<len(n)<4:
    print("NP")
else:
    stk_list.append(n[0])
    for i in range(1,len(n)):
        if stk_list[-1] =="A" and n[i] =="A":
            break
        if stk_list[-1] =="A" and n[i] =="P":
            stk_list.pop()
            if len(stk_list) == 0:
                break
            stk_list.pop()
            if len(stk_list) == 0:
                break
            stk_list.pop()
        stk_list.append(n[i])

    if len(stk_list)==1 and stk_list[-1]=="P":
        print(str("PPAP"))
    else:
        print(str("NP"))
