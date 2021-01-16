while True:
	sandvich = input('Введите слово для зашифровки : ')
	sand1  = sandvich[0:len(sandvich)//2]
	sand2  = sandvich[len(sandvich)//2:]
	x = 0
	sand = ''
	while x < len(sandvich) // 2:
		ch1 = sand1[x]
		ch2 = sand2[x]
		sand += ch1 + ch2
		x += 1


	print (sand)