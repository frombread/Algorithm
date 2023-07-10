n = int(input())
m = input()
a =""
ans = 0
for i in m:
    if i.isnumeric():
        a = a+str(i)
    else:
        if a != "":
            ans += int(a)
            a=""
if a :
    ans += int(a)
print(ans)