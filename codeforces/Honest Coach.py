t = int(input())

for test in range(t):
    n = int(input())
    s = list(map(int, input().split()))
    
    value = max(s)
    
    for i in range(len(s) - 1):
        for j in range(i + 1, len(s)):
            a = s[i] - s[j]
            if a < 0:
                a *= -1
                
            if a < value:
                value = a
                
    print(value)