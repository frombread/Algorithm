import sys
a= int(input())
stk_list = []


for i in range(a):
    input = sys.stdin.readline().split()
    word = input[0]

    if word== 'pop':
        if len(stk_list) ==0:
            print(-1)
        else:
            result = stk_list.pop()
            print(result)
        
    elif word == 'push':
        value = input[1]
        stk_list.append(value)
    
    elif word == 'top':
        if len(stk_list) ==0:
            print(-1)
        else:
            print(stk_list[-1])

    elif word == 'size':
        print(len(stk_list))

    elif word =="empty":
        if len(stk_list) == 0:
            print(1)
        else:
            print(0)