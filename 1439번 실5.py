s = input()

t_count = 0
f_count = 0

if s[0] == "0":
    t_count += 1
else:
    f_count += 1

for i in range(1, len(s)):
    if s[i] != s[i-1]:
        if s[i] == "0":
            t_count += 1
        else:
            f_count += 1

x = min(t_count, f_count)
print(x)

