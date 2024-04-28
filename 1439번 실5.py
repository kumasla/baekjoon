s = input()

count = 0
t_count = 0
f_count = 0
change = False
int 
i = 1
x = s[1]
if(s[1]!= "0") :f_count += 1
if(s[1]!= "1") : t_count =+1

for i in range(len(s)) :
    if(s[i] != s[i-1]) :
        if(count== 0) : 
            if(s[i] == s[0]) :
                t_count += 1
            elif(s[i]) :
                f_count += 1

x = min(t_count,f_count)
print(x)