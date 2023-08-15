n,m = map(int,input().split())
a = list(map(int, input().split()))
res =[]
for i in range(0,n):
    for j in range(i+1,n):
        for z in range(j+1,n):
            if a[i] + a[j] + a[z] <= m:
                res.append(a[i] + a[j] + a[z])

print(max(res))