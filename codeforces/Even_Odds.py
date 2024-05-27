n, k = map(int, input().split())

l = []

if (n + 1) // 2 >= k:
    # odd
    print(2 * k - 1)
else:
    # even
    print((k - (n + 1) // 2) * 2)