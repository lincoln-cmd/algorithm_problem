n, m = map(int, input().split())

column = [[] for _ in range(n)]
black = ['W', 'G', 'B']


for i in range(n):
    column[i] = list(map(str, input().split()))
    

def color(n, m, column, black):
    check = True
    for i in range(n):
        for j in range(m):
            if column[i][j] not in black:
                return '#Color'
    return '#Black&White'
        
    
print(color(n, m, column, black))