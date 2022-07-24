n, h = map(int, input().split())
 
list1 = list(map(int, input().split()))
 
count = 0
 
for i in list1:
    if i > h:
        count += 2
    else:
        count += 1
        
print(count)