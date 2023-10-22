def solution(s, n):
    answer = ''
    list1 = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    list2 = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

    for i in s:
        for j in range(len(list1)):
            if i == list1[j]:
                if j+n > len(list1)-1:
                    answer += list1[j+n-len(list1)]
                else:
                    answer += list1[j+n]
            elif i ==list2[j]:
                if j+n > len(list1)-1:
                    answer += list2[j+n-len(list2)]
                else:
                    answer += list2[j+n]
            elif i == " ":
                answer+=" "
                break
    return answer