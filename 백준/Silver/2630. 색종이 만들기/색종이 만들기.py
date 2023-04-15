"""색종이 만들기"""
def color_paper(x,y,n):
    global blue, white
    color = paper[x][y]
    for i in range(x, x+n):
        for j in range(y,y+n):
            if color != paper[i][j]:
                color_paper(x,y,n//2)
                color_paper(x,y+n//2,n//2)
                color_paper(x+n//2,y+n//2,n//2)
                color_paper(x+n//2,y,n//2)
                return
            
    if color ==0:
        white +=1
    else:
        blue+=1

import sys
n= int(input())
paper =[list(map(int, sys.stdin.readline().split())) for _ in range(n)]
blue, white =0,0

color_paper(0,0,n)
print(white,blue,sep="\n")
