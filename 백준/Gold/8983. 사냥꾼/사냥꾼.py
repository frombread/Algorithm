
def binary_function(gun_x,animal_x,animal_y):
    global count
    pl=0
    pr=len(gun_x)-1

    while pl<=pr:
        pc = (pl+pr)//2
        if distance_func(animal_x,animal_y,pc) <=dis:
            count+=1
            return
        else:
            if animal_x< gun_x[pc]:
                pr=pc-1
            else:
                pl=pc+1
            

def distance_func(animal_x,animal_y,pc):
    return abs(animal_x-gun_x[pc])+animal_y

import sys
gun, animal, dis= map(int,sys.stdin.readline().split())
gun_x =list(map(int,sys.stdin.readline().split()))
distance_list =[]
animals=[]
gun_x.sort()

count =0

for a in range(animal):
    animal_x,animal_y = map(int,sys.stdin.readline().split())
    animals.append([animal_x,animal_y])
    
for i in animals:
    binary_function(gun_x,i[0],i[1])

print(count)

