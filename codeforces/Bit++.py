import sys
 
input = sys.stdin.readline
 
n = int(input())
 
x = 0 
for i in range(n):
    s = str(input())
    if '++' in s:
        x += 1
    else:
        x -= 1
            
print(x)