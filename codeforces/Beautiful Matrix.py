import sys
 
input = sys.stdin.readline
 
a, b = 0, 0
 
for i in range(5):
    m = list(map(int, input().split()))
    if 1 in m:
        a += i + 1
        b = m.index(1) + 1
        
if a <= 3:
    a = 3 - a
elif 3 < a <= 5:
    a = a - 3
    
if b <= 3:
    b = 3 - b
elif 3 < b <= 5:
    b = b - 3
    
print(a+b)