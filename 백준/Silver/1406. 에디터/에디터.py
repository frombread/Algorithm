m = list(input())
n = int(input())
list_ =[]
# Cursor
cursor = len(m)
for _ in range(n):
    a = input().split()
    if a[0]=="L":
        if len(m) > 0:
            list_.append(m.pop())
    elif a[0] == "D":
        if len(list_) > 0:
            m.append(list_.pop())
    elif a[0] == "B":
        if len(m)>0:
            m.pop()
    elif a[0] =="P":
        m.append(a[1])
list_.reverse()
res = m+list_
print("".join(res))