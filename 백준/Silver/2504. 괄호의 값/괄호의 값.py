import sys

ps = sys.stdin.readline()


stk_list =[]

tmp =1
res =0

for i in range(len(ps)):
    bracket = ps[i]
    if bracket=="(":
        tmp *= 2
        stk_list.append(bracket)
    elif bracket == "[":    
        tmp *= 3
        stk_list.append(bracket)

    elif bracket ==")":
        if not stk_list or stk_list[-1]=="[":
            res =0
            break
        if ps[i-1] =="(":
            res += tmp
        tmp//=2
        stk_list.pop()
    
    elif bracket =="]":
        if not stk_list or stk_list[-1]=="(":
            res = 0
            break
        if ps[i-1] =="[":
            res += tmp
        tmp//=3
        stk_list.pop()

if stk_list:
    res=0
print(res)    

