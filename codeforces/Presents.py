n = int(input())
 
list1 = list(map(int, input().split()))
 
list2 = [None] * n
 
for i, j in enumerate(list1):
    list2[j - 1] = i + 1
        
for i in list2:
    print(i, end = ' ')