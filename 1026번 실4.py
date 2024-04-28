N = int(input())

# 첫 번째 줄 입력 받기
a = list(map(int, input().split()))

# 두 번째 줄 입력 받기
b = list(map(int, input().split()))

a_index = [index for index, value in sorted(enumerate(a), key=lambda x: x[1])]
b_index = [index for index, value in sorted(enumerate(b), key=lambda x: x[1],reverse = True)]
new = [0]*N
for i, (x,y)in enumerate(zip(b_index, a_index)) :
    new[x] = a[y]

print(new)
print("a:", a)
print("b:", b)
