n = int(input("Введите число, чтобы узнать простое ли оно: "))
i = 2
numb = ''
while i < n:
	if n % i != 0:
		numb = 1
	else:
		numb = 0
		break
	i += 1
 
if numb == 1:
	print("Число простое")
else:
	print("Число не простое")
input()