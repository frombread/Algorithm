math_list = list(input())

num_list =[]
num = ""
ans =0
button =False
for i in math_list:
    if '0'<=i<='9':
        num+=i
    else:
        if button ==True:
            ans -=int(num)
        else:
            ans +=int(num)

        if i =="-":
            button =True
        num =""

if button ==True:
    ans -=int(num)
else:
     ans +=int(num)
print(ans)