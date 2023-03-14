# codefoces 1454A

t = int(input())

for test in range(t):
    n = int(input())
    
    li = list(i for i in range(1, n + 1))
    a = li.append(li.pop(0))
    
    print(*li)