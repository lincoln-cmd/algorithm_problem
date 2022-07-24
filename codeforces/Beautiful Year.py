y = int(input())
 
while True:
    y += 1
    s = set()
    for i in str(y):
        s.add(i)
        
    if len(s) == len(str(y)):
        print(y)
        break