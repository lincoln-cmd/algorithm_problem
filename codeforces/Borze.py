borze = list(str(input()))

answer = ''

while borze:
    a = borze.pop(0)
    if a == '.':
        answer += '0'
    else:
        b = borze.pop(0)
        if b == '.':
            answer += '1'
        else:
            answer += '2'
            
print(answer)