a = list(map(int, input().split()))

s = str(input())

calories = 0

for i in range(len(s)):
    calories += a[int(s[i]) - 1]
    
print(calories)