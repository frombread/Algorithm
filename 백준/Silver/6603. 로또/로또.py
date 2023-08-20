def permutation(idx, str_, depth):
    flag[idx]=True
    str_ = str_+ str(s_list[idx])

    if depth == 5:
        ans.append(str_)
        return
    str_ = str_+ " "

    for i in range(len(s_list)):
        if flag[i]==False:
            permutation(i,str_,depth+1)
            flag[i]=False

test=[]
cnt =0
while True:
    S = list(map(int, input().split()))
    if S[0] == 0:
        break
    test.append(S)

for S in test:
    n = S[0]
    s_list = S[1:]
    flag=[False]*n
    ans =[]
    res =[]
    woo=[]
    for i in range(n):
        permutation(i,"",0)

    for i in ans:
        a = list(map(int,i.split()))
        a.sort()
        sorted_str = ''.join(map(str, a))
        if sorted_str not in woo:
            res.append(a)
            woo.append(sorted_str)
    for i in res:
        print(' '.join(map(str,i)))

    if cnt !=len(test)-1:
        cnt +=1
        print(" ")
