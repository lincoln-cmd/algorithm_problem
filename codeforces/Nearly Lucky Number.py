n = int(input())
 
a = str(n).count('4') + str(n).count('7')
 
#s = set()
 
#for i in str(n):
 #   s.add(i)

if a == 4 or a == 7:
    print('YES')
else:
    print('NO')