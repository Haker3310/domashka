
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
	if user == 1 and bot == 2:
		print('Вы выиграли!')
		user_score +=1
	if user == 2 and bot == 3:
		print('Вы выиграли!')
		user_score +=1
	if user == 3 and bot == 1:
		print('Вы выиграли!')
		user_score +=1

	if bot == 1 and user == 2:
		print('Вы проиграли!')
		bot_score +=1
	if bot == 2 and user == 3:
		print('Вы проиграли!')
		bot_score +=1
	if bot == 3 and user == 1:
		print('Вы проиграли!')
		bot_score +=1
	print ('bot:', bot_score, '  Вы:', user_score)
if bot_score < user_score:
	print('Вы Победили бота!')
else:
	print('Вы проиграли боту!')
print('Игра окончена!')
input()