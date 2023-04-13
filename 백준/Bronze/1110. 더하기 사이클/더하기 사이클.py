n= int(input())
count =0
# def sum(a,back_num):
#     global count
#     z=(a%10) ## 십자리
#     y = ((a%100)-z)//10 ## 일자리
#     back_num = (z+y)%10

#     sum_num = z + y
#     if z+y == a:
#         return 1
#     else :
#         count +=1
        
#         sum(sum_num+z,back_num)
    
# sum(a,0)
# print(print(count))

num =n
while True :
    a=num//10
    b=num%10 
    c=(a+b)%10
    num = (b*10)+c
    count = count +1
    if (num == n):
        break
    
print(count)



