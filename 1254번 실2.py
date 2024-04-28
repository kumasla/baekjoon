s = input()

for i in range(len(s)) : 
    # s[i:] == s[i]~s[len(s)] 
    # s[i:][::-1] == reversed(s[i:]) s[i]~s[len(s)] 뒤집기
    # 그럼 i는 회문의 길이 문자 길이 + 회문의 길이는 최소 길이
    if s[i:] == s[i:][::-1]: 
        print(len(s)+i)
        break