t = int(input())

for i in range(t):
    x, y, n = map(int, input().split())
    a = n % x
    if a > y:
        print(n - a + y)
    elif a == y:
        print(n)
    else:
        print(n - a - x + y)