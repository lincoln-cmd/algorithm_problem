t = int(input())
 
for test in range(t):
    a, b, c = map(int, input().split())
    
    print('+' if a + b == c else '-')