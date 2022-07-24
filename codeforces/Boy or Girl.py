s = str(input())
    
list1 = []
    
for i in s:
    if i not in list1:
        list1.append(i)
            

if len(list1) % 2 == 0:
    print('CHAT WITH HER!')
else:
    print('IGNORE HIM!')