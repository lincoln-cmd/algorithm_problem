#import sys
 
#input = sys.stdin.readline
 
n = int(input())
 
list1 = [str(input()) for _ in range(n)]
 
list2 = []
 
for i in list1:
    if len(i) > 10:
        i = i[0] + str(len(i) - 2) + i[-1]
        list2.append(i)
    else:
        list2.append(i)
        
for i in list2:
    print(i)
