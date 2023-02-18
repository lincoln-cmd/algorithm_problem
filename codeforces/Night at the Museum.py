import string


n = list(str(input()))

alphabet = list(string.ascii_lowercase)

pointer = 0
cnt = 0



while n:
    a = n.pop(0)
    if alphabet.index(a) - pointer < 0:
        space = -1 * (alphabet.index(a) - pointer)
    else:
        space = alphabet.index(a) - pointer
        
    
    if space < 13:
        cnt += space
        pointer = alphabet.index(a)
    else:
        cnt += (26 - space)
        pointer = alphabet.index(a)
    
    
print(cnt)