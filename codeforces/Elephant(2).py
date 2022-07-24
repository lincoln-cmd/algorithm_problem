x = int(input())
 
count = 0
 
a, b = divmod(x, 5)
 
if b > 0:
    count += (a + 1)
else:
    count = a
    
print(count)