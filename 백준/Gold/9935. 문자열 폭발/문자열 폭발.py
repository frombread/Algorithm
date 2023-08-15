sentence = list(input())

bomb = input()

list_1 = []


for i in sentence:
    list_1.append(i)
    if len(list_1) >= len(bomb):
        if ''.join(list_1[-len(bomb):]) == bomb:
            for _ in range(len(bomb)):
                list_1.pop()


if len(list_1)==0:
    print("FRULA")
else:
    print(''.join(list_1))

