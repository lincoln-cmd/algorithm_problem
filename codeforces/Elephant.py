x = int(input())
 
count = 0
 
while x:
    if x >= 5:
        x -= 5
        count += 1
    else:
        x = 0
        count += 1
        
print(count)