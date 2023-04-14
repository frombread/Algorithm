def binary_search(list,key):

    pl =0
    pr = len(list)-1

    while True:
        pc = (pl+pr)//2
        
        if list[pc] == key:
            return 1
        
        elif list[pc]< key:
            pl = pc + 1
        else:
            pr = pc-1

        if pl > pr:
            break
    return 0

fake =int(input())
fake_list= list(map(int,input().split()))
real = int(input())
real_list= list(map(int,input().split()))

fake_list.sort()
for i in real_list:
    print(binary_search(fake_list,i))
