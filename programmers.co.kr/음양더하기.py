def solution(absolutes, signs):
    for i, j in enumerate(signs):
        if j != True:
            absolutes[i] *= -1
            
            
    return sum(absolutes)