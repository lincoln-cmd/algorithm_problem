n = int(input())

level = 0
cnt = 0


for i in range(1, n + 1):
    for j in range(1, i + 1):
        cnt += j
    if cnt <= n:
        level += 1
    else:
        break
        
print(level)