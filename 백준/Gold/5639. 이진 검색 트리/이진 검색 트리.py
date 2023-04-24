import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
tree=[]
while True:
    try:
        tree.append(int(input()))
    except:
        break

def postorder(first, end):
    if first > end :
        return

    mid = end + 1

    for i in range(first+1, end+1):
        if tree[first] < tree[i]:
            mid = i
            break
    
    postorder(first+1,mid-1)
    postorder(mid,end)
    print(tree[first])

postorder(0,len(tree)-1)