ax,ay,bx,by,cx,cy = map(int,input().split())

ab_len = ((ax-bx)**2 + (ay-by)**2)**0.5
ac_len = ((ax-cx)**2 + (ay-cy)**2)**0.5
bc_len = ((bx-cx)**2 + (by-cy)**2)**0.5

length = [ab_len+ac_len, ab_len + bc_len, ac_len+bc_len]
result = 2*(max(length) - min(length))
if ((ax-bx)*(ay-cy)==(ay-by)*(ax-cx)):
    result = -1

print(result)