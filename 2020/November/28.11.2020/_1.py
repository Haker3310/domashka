while True:
	stroka = input('Введите строку : ')
	while stroka.find('/*') != -1 or stroka.find('*/') != -1:
		f1= stroka.find('/*')	
		f2= stroka.find('*/')
		delete = stroka[f1: f2 + 2]
		stroka = stroka.replace(delete, ' ')
	print (stroka)