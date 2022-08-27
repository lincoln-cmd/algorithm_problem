t = int(input())

for test in range(t):
    n = int(input())
    
    c1, c2 = 1, 2
    
    quotient = n // (c1 + c2)
    remainder = n % (c1 + c2)
    
    if remainder == 1:
        c1, c2 = quotient + 1, quotient
    elif remainder == 2:
        c1, c2 = quotient, quotient + 1
    else:
        c1, c2 = quotient, quotient
        
    print(c1, c2)