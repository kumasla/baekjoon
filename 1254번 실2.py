s = input()

max = len(s)

result = 0 

i,j = 0, max-1

half = max // 2
count = 0
check = True

if max % 2 != 0 : 
    half + 1
    check = False

while i < j :
    if s[i] == s[j] :
        count += 1
        i += 1
        j -= 1
    else : i += 1

if count == half : result = max
elif count == 0 : 
    if check == True :
        result = max *2 - 1
    else : 
        result = max * 2
else :
    if max - j  < 0: 
        result = count
    else : 
        result = max + (max - count*2)


print(result)
print(count)