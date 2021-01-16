while True:
	y = 0
	sandvich = input('Введите слово для разшифровки : ')
	while y != len(sandvich)//2:
		y += 1
		x = 0
		sand = ''
		sand1  = sandvich[0:len(sandvich)//2]
		sand2  = sandvich[len(sandvich)//2:]
		x1 = len(sandvich)//2
		x1+= len(sandvich)//3
		while x != x1:
			ch1 = sand1[x]
			ch2 = sand2[x]
			sand += ch1 + ch2
			x += 1
	sandvich = sand


	print (sand)