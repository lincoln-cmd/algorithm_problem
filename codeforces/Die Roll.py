from fractions import Fraction

y, w = map(int, input().split())

highest = max(y, w)

probability = Fraction((6 - highest + 1), 6)

if probability <= 0:
    print('0 / 1')
elif probability >= 1:
    print('1 / 1')
else:
    print(probability)