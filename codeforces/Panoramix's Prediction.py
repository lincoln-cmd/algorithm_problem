n, m = map(int, input().split())

answer = 'YES'

for i in range(n + 1, m):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        answer = 'NO'
            
for i in range(2, m):
    if m % i == 0:
        answer = 'NO'
        break

                
print(answer)