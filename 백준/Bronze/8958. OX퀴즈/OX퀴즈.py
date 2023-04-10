import sys
x=int(sys.stdin.readline())
for _ in range(x):
    b=0
    c=0
    a=str(sys.stdin.readline())
    for y in a:
       if y == "O":
           b += 1
           c += b
       else:
           b =0
    print(c)
