t = int(input())

for test in range(t):
    rating = int(input())
    
    if rating >= 1900:
        print('Division 1')
    elif 1600 <= rating < 1900:
        print('Division 2')
    elif 1400 <= rating < 1500:
        print('Division 3')
    else:
        print('division 4')