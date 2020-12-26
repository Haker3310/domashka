

def win(x, y):
	global user_score
	if user == x and bot == y:
		print('Вы выиграли!')
		user_score = user_score + 1

def lose(x, y):
	global bot_score
	if bot == x and user == y:
		print('Вы проиграли!')
		bot_score = bot_score + 1

import random
wins = int(input('Введите до скольки побед хотите играть: '))
bot_score = 0
user_score = 0
while wins > 0:
	if bot_score == wins or user_score == wins:
		break
	user = int(input('1 - камень, 2 - ножницы, 3 - бумага: '))
	bot = int(random.randint(1,3))
	if user == 1 and bot == 1 or user == 2 and bot == 2 or user == 3 and bot == 3:
		print('Ничья!')
	win(1,2)
	win(2,3)
	win(3,1)

	lose(1,2)
	lose(2,3)
	lose(3,1)
	print ('bot:', bot_score, '  Вы:', user_score)
if bot_score < user_score:
	print('Вы Победили бота!')
else:
	print('Вы проиграли боту!')
print('Игра окончена!')
input()