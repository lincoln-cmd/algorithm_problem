n = int(input())
 
li = []
 
for i in range(n):
    li.append(str(input()))
    
group = 0
 
for i in range(len(li)-1):
    if li[i] == li[i+1]:
        continue
    else:
        group += 1
        
print(group + 1)