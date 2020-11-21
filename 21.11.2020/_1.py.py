password = ''
re_pass = ''

def pas():
	global password
	password = input('Введите пароль : ')
	
def set_pas():
	global set_pas
	re_pass=''
	re_pass = input('Подтвердите пароль : ')
	while re_pass != password:
		print('Пароли не совпадают!')
		re_pass = input('Подтвердите пароль : ')
	print('Пароль сохранен!')

pas()
while True: 
	if 8 > len(password) or 32 < len(password):
		print ('min 8 символов max 32 символа')
		pas()
	if password.find('й')!=-1 or password.find('ц')!=-1 or password.find('у')!=-1 or password.find('к')!=-1 or password.find('е')!=-1 or password.find('н')!=-1 or password.find('г')!=-1 or password.find('ш')!=-1 or password.find('щ')!=-1 or password.find('з')!=-1 or password.find('х')!=-1 or password.find('ъ')!=-1 or password.find('ф')!=-1 or password.find('ы')!=-1 or password.find('в')!=-1 or password.find('а')!=-1 or password.find('п')!=-1 or password.find('р')!=-1 or password.find('о')!=-1 or password.find('л')!=-1 or password.find('д')!=-1 or password.find('ж')!=-1 or password.find('э')!=-1 or password.find('я')!=-1 or password.find('ч')!=-1 or password.find('с')!=-1 or password.find('м')!=-1 or password.find('и')!=-1 or password.find('т')!=-1 or password.find('ь')!=-1 or password.find('б')!=-1 or password.find('ю')!=-1 or password.find('Й')!=-1 or password.find('Ц')!=-1 or password.find('У')!=-1 or password.find('К')!=-1 or password.find('Е')!=-1 or password.find('Н')!=-1 or password.find('Г')!=-1 or password.find('Ш')!=-1 or password.find('Щ')!=-1 or password.find('З')!=-1 or password.find('Х')!=-1 or password.find('Ъ')!=-1 or password.find('Ф')!=-1 or password.find('Ы')!=-1 or password.find('В')!=-1 or password.find('А')!=-1 or password.find('П')!=-1 or password.find('Р')!=-1 or password.find('О')!=-1 or password.find('Л')!=-1 or password.find('Д')!=-1 or password.find('Ж')!=-1 or password.find('Э')!=-1 or password.find('Я')!=-1 or password.find('Ч')!=-1 or password.find('С')!=-1 or password.find('М')!=-1 or password.find('И')!=-1 or password.find('Т')!=-1 or password.find('Ь')!=-1 or password.find('Б')!=-1 or password.find('Ю')!=-1 or password.find('ё')!=-1 or password.find('Ё')!=-1:
		print ('Пароль введен не верно!')
		pas()
	else:
		set_pas()
		break
	if password.find('"')!=-1 or password.find("'")!=-1 or password.find(';')!=-1 or password.find(':')!=-1 or password.find('[')!=-1 or password.find(']')!=-1 or password.find('{')!=-1 or password.find('}')!=-1 or password.find('|')!=-1 or password.find('/')!=-1 or password.find('<')!=-1 or password.find('>')!=-1 or password.find(',')!=-1 or password.find('!')!=-1 or password.find('+')!=-1 or password.find('_')!=-1 or password.find(')')!=-1 or password.find('(')!=-1 or password.find('*')!=-1 or password.find('&')!=-1 or password.find('^')!=-1 or password.find('?')!=-1 or password.find('%')!=-1 or password.find('$')!=-1 or password.find('#')!=-1 or password.find('№')!=-1 or password.find('=')!=-1 or password.find('`')!=-1 or password.find('~')!=-1:
		print('Символы ";:<>!?/\,*-+()&^%$№#=_~` запрещены!')
		pas()
	else:
		set_pas()
		break
