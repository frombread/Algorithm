n = int(input())

answer = 0
res =[]
for i in range(1,n+1):
    answer += i
    a = list(str(i))
    for j in range(len(a)):
        answer +=int(a[j])
    if answer == n:
        res.append(i)
        break
    else:
        answer = 0

if res:
    print(min(res))
else:
    print(0)





