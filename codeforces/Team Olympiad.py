n = int(input())


t = list(map(int, input().split()))
cnt1, cnt2, cnt3 = t.count(1), t.count(2), t.count(3)

min_num = min(cnt1, cnt2, cnt3)

if cnt1 == 0 or cnt2 == 0 or cnt3 == 0:
		print(0)
else:
	li = []
    
	while cnt1 and cnt2 and cnt3:
		one = t.index(1)
		t[one] = 0
		#print(t)
		two = t.index(2)
		t[two] = 0
		three = t.index(3)
		t[three] = 0
		cnt1 -= 1
		cnt2 -= 1
		cnt3 -= 1
		li.append(one + 1)
		li.append(two + 1)
		li.append(three + 1)
    
	print(min_num)
	for i in range(0, len(li), 3):
		print(li[i], li[i + 1], li[i + 2])