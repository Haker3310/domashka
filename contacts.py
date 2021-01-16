import sqlite3, os, time, argparse

con = sqlite3.connect("cont_book.db")
cursor = con.cursor()
vvod = ''
'''parser = argparse.ArgumentParser(description='Контактная книга')

parser.add_argument('-s', '--see',default=1)
args = parser.parse_args()

if args.see:
	cursor.execute('SELECT name, phone FROM contacts')
	numb = 0
	for contact in cursor:
		numb +=1
		print(numb,'-', contact)
	if numb == 0:
		print('Номеров нет!')
else:
	pass
'''
class Cont_book():
	def __init__(self):
		try:
			cursor.execute('CREATE TABLE contacts(Name TEXT, phone TEXT)')
		except sqlite3.OperationalError:
			pass

	def add():
		name = input('Имя - ')
		number = input('Телефон - ')
		cursor.execute('INSERT INTO contacts(name, phone) VALUES(?,?)', (name, number))

		con.commit()

	def remove():
		name = input('Введите имя которое хотите удалить - ')
		cursor.execute('DELETE FROM contacts WHERE name=?', [name])

	def see():
		cursor.execute('SELECT name, phone FROM contacts')
		numb = 0
		for contact in cursor:
			numb +=1
			print(numb,'-', contact)
		if numb == 0:
			print('Номеров нет!')
		print()
		input('Нажмите "Enter" чтобы продолжить ')
		con.commit()

	def save():
		print('Изменения были сохранены')
		con.commit()

class Menu(Cont_book):
	def __init__(self):
		time.sleep(0.5)
		os.system ('cls')
		print('''
 ___________________________________
|                                   |
|    add - добавить контакт         |
|    remove - удалить контакт       |
|    see - показать все контакты    |
|___________________________________|
			  ''')
		vvod = input()
		if vvod == 'add':
			Cont_book.add()
		if vvod == 'remove':
			Cont_book.remove()
		if vvod == 'see':
			Cont_book.see()
		if vvod == 'save':
			Cont_book.save()

Cont_book()
while True:
	Menu()