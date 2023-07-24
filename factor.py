#輸入ㄧ個數字並輸出其所有因數(指輸出 >= 2的因數)

def factor(n) :
	for i in range(2, n) :
		if n % i == 0 :
			return True
	return False

n = int(input('input a number :'))
num = []

for i in range(2, n + 1) :
	if n % i == 0 :
		num.append(i)

print(num)