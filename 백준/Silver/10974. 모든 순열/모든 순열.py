def permutation(idx, str_, depth):
    str_ = str_+ str(list_[idx])
    flag[idx] =True

    if depth == len(list_)-1:
        print(str_)
        return
    str_=str_+ " "

    for i in range(len(list_)):
        if flag[i]==False:
            permutation(i,str_,depth+1)
            flag[i] = False

n = int(input())
list_ =[]
for i in range(1,n+1):
    list_.append(i)

flag =[False] * len(list_)
final_list =[]

for i in range(n):
    permutation(i, "", 0)
    flag[i]=False
