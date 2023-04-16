def binary_search(list2,key):
    floor,roof=0,sum(tree_list)
    while True:
        mid_tree = (floor+roof)//2
        cut = 0
        for i in list2:
            if i>mid_tree:
                cut += i- mid_tree
        if cut>=key:   
            floor = mid_tree +1
        else:
            roof =mid_tree -1
        if floor > roof:
            break
    return roof


import sys
n, high = map(int,sys.stdin.readline().split())
tree_list =list(map(int,sys.stdin.readline().split()))

print(binary_search(tree_list,high))