n=int(input())

def move(n,a,c):
    if n == 1:
        print(a,c)
    else:
        move(n-1,a,6-a-c)
        print(a,c)
        move(n-1,6-a-c,c)

def move_count(n):
    if n == 1:
        return 1
    return (2*(move_count(n-1))+1)

print(move_count(n))
if n <= 20: move(n,1,3)
