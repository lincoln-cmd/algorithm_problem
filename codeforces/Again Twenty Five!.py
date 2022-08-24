n = int(input())

print(25)

'''
 Explanation
 
  The range of n is that: 2 <= n <= 2 * 10^18.
 We want to find the last two digit of 5^n.
 The results of 5^n is that: 1, 5, 25, 125, 625, 3125, ...
 However, the scope of the n starts from 2, which means that all the result is ended with '25'(25, 125, 625, 3125, ...).
'''