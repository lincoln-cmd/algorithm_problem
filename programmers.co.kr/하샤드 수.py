def solution(x):
    a = 0
    for i in list(str(x)):
        a += int(i)
    if x % a == 0:
        return True
    else:
        return False