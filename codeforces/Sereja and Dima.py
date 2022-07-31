n = int(input())

card = list(map(int, input().split()))

turn = 0
num = [0, 0]


while card:
    if card[0] > card[-1]:
        if turn % 2 == 0:
            num[0] += card.pop(0)
            turn += 1
        else:
            num[1] += card.pop(0)
            turn += 1
    else:
        if turn % 2 == 0:
            num[0] += card.pop(-1)
            turn += 1
        else:
            num[1] += card.pop(-1)
            turn += 1
            
print(num[0], num[1])