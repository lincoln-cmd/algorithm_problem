s = str(input())
 
u, l = 0, 0
 
for i in s:
    if i == i.upper():
        u += 1
    else:
        l += 1
        
if u > l:
    print(s.upper())
else:
    print(s.lower())