n = 11
v = 0
print ('Робот повернут на север')
print ('введите 0 чтобы идти дальше')
print ('введите -1 чтобы повернуть налево')
print ('введите 1 чтобы повернуть направо')
while True:

	v = input('введите 0, 1 или -1 : ')#указать направление
	
	if v == ('0'):
		n = n

	elif v == ('1'):
		n += 1

	elif v == ('-1'):
		n -= 1

	if n == 10: #Чтобы числа были только в нужном диапозоне иначе программа будет работать некорректно
		n = 14

	if n == 15: 
		n = 11

	if n == 11: #Проверка направления
		print ('Робот повернут на север')

	elif n == 12:
		print ('Робот повернут на запад')

	elif n == 13:
		print ('Робот повернут на юг')

	elif n == 14:
		print ('Робот повернут на восток')