import random
start = input('請輸入範圍初始值: ')
end = input('請輸入範圍最終值: ')
start = int(start)
end = int(end)
r = random.randint(start, end)
count = 0
while True:
	count = count + 1
	num = input('請猜數字: ')
	num = int(num)
	if num == r:
		print('終於猜對了')
		print('這是你猜的第', count, '次')
		break
	elif num > r:
		print('比答案大')
	elif num < r:
		print('比答案小')
	print('這是你猜的第', count, '次')