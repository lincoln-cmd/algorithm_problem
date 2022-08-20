t = int(input())

for test in range(t):
    n = int(input())
    
    
    print(n // 2)
    
    
    '''
    Explanation
    
    
     The result we want to get is maximum value of greatest common divisor(gcd) of A and B. Those numbers are in range n(1 <= A < B <= n). For this, it is possible to get the result if the divided number is larger. In other words, the larger the divided number, the larger the gcd value. For instance, if there are two numbers 8 and 10, two divisors i and j, and two instances x and y. We want to get maximum value of divisor between i and j.
     Suppose 8 / i = x and 10 / j = y. -> 8 / x = i and 10 / y = j.
     In this suppose, if x and y is being lower, i and j is being larger. Therefore, we can get maxmimum gcd value if given number is even number because all the even numbers are devided by 2 and j is bigger than i becase 10 is bigger than 8. However, if given number is odd number, we cannot divede that with 2, but that's divisor is comparable with a number 1 less than given number. This is because the former even number's divisor has same one of latter odd number's.
     For example, if given number is 15, quotient of it is 7, but 14 has also has same quotient.
     -> 21 // 2 = 10 === 20 // 2 == 10
     -> 99 // 2 = 49 === 98 // 2 == 49.....
     '''