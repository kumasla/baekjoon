s = input()

t_count = 0
f_count = 0

# 첫 번째 문자와 같은지 확인하여 초기값 설정
if s[0] == "0":
    t_count += 1
else:
    f_count += 1

# 두 번째 문자부터 끝까지 반복하여 카운트
for i in range(1, len(s)):
    # 현재 문자와 이전 문자가 다르면 카운트 증가
    if s[i] != s[i-1]:
        if s[i] == "0":
            t_count += 1
        else:
            f_count += 1

# 두 카운트 중 작은 값을 선택하여 출력
x = min(t_count, f_count)
print(x)

