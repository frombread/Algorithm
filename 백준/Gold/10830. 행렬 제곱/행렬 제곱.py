import sys

n,b=map(int, sys.stdin.readline().split())
matrix_list =[]
for _ in range(n):
    matrix_list.append(list(map(int,sys.stdin.readline().split())))



def mul_metrix(m1,m2):
    result = [[0]* n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for z in range(n):
                result[i][j] += m1[i][z] * m2[z][j] %1000
    return result

def metrix_func(a, q):
    if q==1:
        return a
    else:
        tmp = metrix_func(a, q//2)
        if q%2 ==0:
            return mul_metrix(tmp,tmp)
        else: 
            return mul_metrix(mul_metrix(tmp,tmp),a)
        
result = metrix_func(matrix_list,b)

for row in result:
    for cor in row:
        print(cor %1000 , end=" ")
    print()