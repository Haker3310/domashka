#В данном натуральном числе найдите количество цифр, которые больше 3, но меньше 8

#a = input("введите число:")
#s = a.count('3')
#s += a.count('4')
#s += a.count('5')
#s += a.count('6')
#s += a.count('7')
#s += a.count('8')
#print (s)

#a = input('Введите числo: ')
#y = 0
#x = 3
#while x < 8:
# y += a.count(str(x))
# x += 1
#print(y)

#a = input('Ввведте числo ')
#y = 0
#y += a.count('3') + a.count('4') + a.count('5') + a.count('6') + a.count('7') + a.count('8') 
#print (y)

a = input('Введите числo: ')
a = a.count('3') + a.count('4') + a.count('5') + a.count('6') + a.count('7') + a.count('8') 
print (a)