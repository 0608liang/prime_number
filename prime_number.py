#寫一個能判別質數的程式
#輸入ㄧ個數字判斷其是否為質數


#return ... 會回報結果並停止程式繼續
def prime_number(n) :
	for i in range(2, n) :
		if n % i == 0 :
			return False
	return True

n = int(input('input a number in 2 ~ 1000 :'))
if n <= 2 :
	print('please input a higher number!!')
	raise SystemExit
elif n > 1000 :
	print('please input a lower number!!')
	raise SystemExit

for i in range(2, n) :
	if prime_number(n) == True :
		print(str(n) + ' ' + 'is a prime number!!')
		break
	else :
		print(str(n) + ' ' + 'is not a prime number!!')
		break