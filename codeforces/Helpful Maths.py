import sys
 
input = sys.stdin.readline
 
s = sorted(list(map(int, input().split('+'))))
 
print(*s, sep = '+')