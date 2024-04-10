t = 1

for test in range(t):
    a, b, c = map(int, input().split())
    
    print('YES' if sum(sorted([a, b, c], reverse = True)[:2]) >= 10 else 'No')