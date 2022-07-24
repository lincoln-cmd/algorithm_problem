n = int(input())
 
tram = 0
mini = 0
 
for i in range(n):
    ex, en = map(int, input().split())
    
    tram += (en - ex)
    if tram > mini: mini = tram
    
print(mini)