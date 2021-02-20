
import random


c1 = int(input('Введите шанс на появление числа 1 : '))
c2 = int(input('Введите шанс на появление числа 2 : '))
c3 = int(input('Введите шанс на появление числа 3 : '))



while True:


	print('Шансы ',c1,':',c2,':',c3,' ')
	change_c=input()
	if change_c == 'c':
		c1 = int(input('Введите шанс на появление числа 1 : '))
		c2 = int(input('Введите шанс на появление числа 2 : '))
		c3 = int(input('Введите шанс на появление числа 3 : '))
	c_max = c1+c2+c3

	print('     -----------------------')
	print('     | ', end='')

	for i in 'iiiiiiiiii':
		chanse = random.randint(1,c_max)

		if 0<chanse<c1+1:
			print(1, end=' ')

		if c1<chanse<c1+c2+1:
			print(2, end=' ')

		if c1+c2<chanse<c1+c2+c3+1:
			print(3, end=' ')

		chanse = 0

	print('|')
	print('     -----------------------')