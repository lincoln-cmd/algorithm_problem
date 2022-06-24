m, n = map(int, input().split())
 
a = m // 2
b = n // 1
 
m -= (a * 2)
 
if m >= 1 and n >= 2:
    c = m // 1
    d = n // 2
else:
    c, d = 0, 0
    
print((a * b) + (c * d))