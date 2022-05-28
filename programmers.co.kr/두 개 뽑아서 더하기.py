def solution(numbers):
    length = len(numbers)
    s = set()
    for i in range(0, length):
        for j in range(i + 1, length):
            s.add(numbers[i] + numbers[j])
    l = list(s)
    l.sort()
    answer = l
    return answer

if __name__ == "__main__":
    numbers = [2,1,3,4,1]
    solution(numbers)