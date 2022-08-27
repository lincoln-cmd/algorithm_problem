n = int(input())

if n % 2 == 0:
    cnt = n // 2
    li = [2 for i in range(cnt)]
else:
    cnt = (n - 3) // 2
    li = [2 for i in range(cnt)]
    li.append(3)
    cnt += 1
        
print(cnt)
for i in range(len(li)):
    print(li[i], end = ' ')

    
'''
 We only consider 2 and 3 because those numbers are the smallest numbers of prime numbers.
'''