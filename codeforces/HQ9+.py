p = str(input())

check = ['H', 'Q', '9']

for text in p:
    if text in check:
        print('YES')
        break
else:
    print('NO')