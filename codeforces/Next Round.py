import sys
 
input = sys.stdin.readline
 
n, k = map(int, input().split())
 
p = list(map(int, input().split()))
 
count = 0
for i in p:
    if i >= p[k-1] and i > 0:
        count += 1
        
print(count)