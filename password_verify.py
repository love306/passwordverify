password = 'a1234567'
#X設為1較容易思考，因想訓練邏輯故意設為0
x = 0
while x < 3:
	user_input = input('您好，請輸入密碼： ')
	if user_input == password:
		print('歡迎您')
		break
	else:
		x = x + 1
		if x == 3:
			print('認證失敗')
			break		
		print('輸入錯誤，還剩',3 - x ,'次機會喔')

	