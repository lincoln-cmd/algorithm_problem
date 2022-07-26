t = int(input())

for test in range(t):
    n = int(input())
    
    task = list(str(input()))
    li = []
    check = True
    
    for i in range(len(task) - 1):
        if task[i] not in li:
            li.append(task[i])
        for j in range(i + 1, len(task)):
            if task[i] == task[j]:
                break
            else:
                if task[j] in li:
                    check = False
                    break
                else:
                    li.append(task[j])
                    break
                
    if check:
        print('YES')
    else:
        print('NO')