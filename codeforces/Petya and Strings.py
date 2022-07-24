import sys
 
input = sys.stdin.readline
 
s1 = list(str(input()).lower())
s2 = list(str(input()).lower())
 
while s1:
    a = s1.pop(0)
    b = s2.pop(0)
    if a == b:
        continue
    if ord(a) < ord(b):
        print(-1)
        break
    elif ord(a) > ord(b):
        print(1)
        break
else:
    print(0)