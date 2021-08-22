x = 1
while True :
	password = input('請輸入密碼： ')
	if password == 'a123456':
		print('登入成功')
		break
	elif x < 2:
		print('密碼錯誤！還有2次機會')
		x = x + 1 
	elif x < 3:
		print('密碼錯誤！還有1次機會')
		x = x + 1 
	else:
		print('密碼錯誤！無機會')
		break
