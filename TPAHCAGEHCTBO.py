import random

time = 0
distance = 0
km_sec = 0
weather = 'good'
gryz_weight = 0

number_of_city_1 = 1
number_of_city_2 = 1

test_ptc = 0

class Citys:
	global distance

	def __init__(self, distance):
		self.distance = distance

	def c(number_of_city_1,number_of_city_2):              #
		distance = 0
		if number_of_city_1 == 1 and number_of_city_2 == 7:# +Автомагистраль
			distance = 70
		if number_of_city_1 == 1 and number_of_city_2 == 8:#
			distance = 80
		if number_of_city_1 == 1 and number_of_city_2 == 9:#
			distance = 90

		if number_of_city_1 == 2 and number_of_city_2 == 7:#
			distance = 110
		if number_of_city_1 == 2 and number_of_city_2 == 8:# +Автомагистраль
			distance = 140
		if number_of_city_1 == 2 and number_of_city_2 == 9:#
			distance = 120

		if number_of_city_1 == 3 and number_of_city_2 == 7:#
			distance = 150
		if number_of_city_1 == 3 and number_of_city_2 == 8:#
			distance = 160
		if number_of_city_1 == 3 and number_of_city_2 == 9:# +Автомагистраль
			distance = 170

		if number_of_city_1 == 4 and number_of_city_2 == 7:# +Автомагистраль
			distance = 210
		if number_of_city_1 == 4 and number_of_city_2 == 8:#
			distance = 200
		if number_of_city_1 == 4 and number_of_city_2 == 9:#
			distance = 240

		if number_of_city_1 == 5 and number_of_city_2 == 7:#
			distance = 320
		if number_of_city_1 == 5 and number_of_city_2 == 8:# +Автомагистраль
			distance = 380
		if number_of_city_1 == 5 and number_of_city_2 == 9:#
			distance = 300

		if number_of_city_1 == 6 and number_of_city_2 == 7:#
			distance = 300
		if number_of_city_1 == 6 and number_of_city_2 == 8:#
			distance = 350
		if number_of_city_1 == 6 and number_of_city_2 == 9:# +Автомагистраль
			distance = 400
		return distance


class Chances:
	global km_sec
	global gryz_weight
	global weather
	global number_of_city_1
	global number_of_city_2

	def __init__():
		self.km_sec = km_sec
		self.gryz_weight = gryz_weight
		self.weather = weather
		self.number_of_city_1
		self.number_of_city_2

	def transports_():
		test_ptc = 0
		while test_ptc != 1:
			P_T_C = random.randint(1,3)
			#CAR
			if P_T_C == 3:
				if gryz_weight < 11:
					test_ptc = 1
					km_sec = 10

			#TRAIN
			if P_T_C == 2:
				if number_of_city_1 == 3 or number_of_city_1 == 4 or number_of_city_1 == 5 or number_of_city_1 == 6:
					if number_of_city_2 == 3 or number_of_city_2 == 4 or number_of_city_2 == 5 or number_of_city_2 == 6:
						if gryz_weight < 26:
							test_ptc = 1
							km_sec = 5

			#PLANE
			if P_T_C == 1:
				if number_of_city_1 == 5 or number_of_city_1 == 6:
					if number_of_city_2 == 5 or number_of_city_2 == 6:
						if weather == 'good':
							if gryz_weight < 21:
								test_ptc = 1
								km_sec = 50

	def weather_():
		weather_B_or_G = ['bad','good']
		weather = random.choice(weather_B_or_G)

	def city_():
		number_of_city_1 = random.randint(7,9)
		number_of_city_2 = random.randint(1,6)
		return number_of_city_1
		return number_of_city_2


class itog:
	global km_sec
	global gryz_weight
	global weather
	global number_of_city_1
	global number_of_city_2
	global time
	def sending():
		Chances.city_()
		Citys.c(number_of_city_1,number_of_city_2)
		Chances.transports_()
		print(distance)
		print(km_sec)
	#	time = distance / km_sec

		print(time)
		print('weather is ', weather)
		print('send from ', number_of_city_1 ,' to ', number_of_city_2)
itog.sending()