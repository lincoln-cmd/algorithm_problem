t = int(input())

for test in range(t):
    n = int(input())
    
    candy = list(map(int, input().split()))
    
    orange = list(map(int, input().split()))
    
    cnt = 0
    min_candy = min(candy)
    min_orange = min(orange)
    
    for i in range(n):
        if candy[i] > min_candy:
            cnt += candy[i] - min_candy
        if orange[i] > min_orange:
            cnt += orange[i] - min_orange
        cnt -= min(candy[i] - min_candy, orange[i] - min_orange)
        
    print(cnt)