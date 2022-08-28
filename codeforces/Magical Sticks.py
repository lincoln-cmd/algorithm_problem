t = int(input())

for test in range(t):
    n = int(input())
    
    li = [i for i in range(1, n + 1)]
    
    if n == 1:
        print(1) # if the number of sticks is only 1, it is impossible to connect
    elif n % 2 == 0:
        print(n // 2) 
        '''
         if the number of sticks is even number, the number of connected sticks is n // 2.
        For example,
        n = 2 -> 1 + 1 => 1
        n = 4 -> 1 + 4, 2 + 3 => 2
        n = 10 -> 1 + 10, 2 + 9, 3 + 8, ... 5 + 6 => 5
        '''
    else:
        print(n // 2 + 1)
        '''
         if the number of sticks is odd number, the number of connected sticks is n // 2 + 1.
          For instance,
          n = 3 -> 1 + 2, 3 => 2
          n = 5 -> 1 + 4, 2 + 3, 5 => 3
          n = 15 -> 1 + 14, 2 + 13, 3 + 12, ..., 15 => 8
        '''