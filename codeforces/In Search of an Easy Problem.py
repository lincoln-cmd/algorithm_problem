n = int(input())
 
li = list(map(int, input().split()))
    
a = li.count(1)
if a == 0:
    print('EASY')
else:
    print('HARD')