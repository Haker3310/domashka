import random
import re

letters = 'abcdefghijklmnopqrstuvwxyz'
text = input('Введите что-нибудь : ')
if len(text) > 2:
	b = text[0] + random.choice(letters) + text[2:]
	text = b
	if len(text) > 5:
		b = text[0:3] + random.choice(letters) + text[5:]
		text = b
		if len(text) > 8:
			b = text[0:5] + random.choice(letters) + text[7:]
			text = b
			if len(text) > 11:
				b = text[0:7] + random.choice(letters) + text[9:]
				text = b

a = re.findall(r'\d\d\d', b)
print(b)
