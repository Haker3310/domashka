import random

numb = 0
chet_nechet = ''
col = 0
element = 0
someList = [random.randint(1, 50) for i in range(random.randint(20, 30))]
def printList(oneList):
    for elem in oneList:
        print(elem, end=' ')
    print()

for i in someList:
	numb +=1
	element +=1
	if numb % 2 == 0:
		del someList[element]


printList(someList)

