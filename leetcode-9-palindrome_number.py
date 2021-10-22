# -*- coding: utf-8 -*-
def solve(x):
    if list(str(x)) == list(reversed(list(str(x)))):
        return True
    else: return False
    
print(solve(121))