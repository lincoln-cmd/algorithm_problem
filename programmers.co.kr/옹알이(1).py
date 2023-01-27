def solution(babbling):
    answer = 0
    
    can = ['aya', 'ye', 'woo', 'ma']
    
    for i in babbling:
        for j in can:
            i = i.replace(j, 'x', 1)
        if len(set(i)) == 1 and 'x' in i:
            answer += 1
            
            
            
    return answer