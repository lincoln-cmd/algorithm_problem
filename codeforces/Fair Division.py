# utilize simple inserting method
t = int(input())

for test in range(t):
    n = int(input())
    
    a = sorted(list(map(int, input().split())), reverse = True)
    
    alice, bob = 0, 0
    
    while a:
        candy = a.pop(0)
        
        if alice <= bob:
            alice += candy
        else:
            bob += candy
            
    print('yes' if alice == bob else 'no')
    
    

    
# utilize mathematical method
t = int(input())

for test in range(t):
    n = int(input())
    
    a = list(map(int, input().split()))
    
    if a.count(2) % 2 == 0 and a.count(1) % 2 == 0:
        print('yes')
    elif a.count(2) % 2 == 1 and a.count(1) % 2 == 0 and a.count(1) > 0:
        print('yes')
    else:
        print('no')
