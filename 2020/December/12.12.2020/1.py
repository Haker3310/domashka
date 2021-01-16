import random

someList = [random.randint(0, 100) for i in range(random.randint(10, 30))]

def sortList(oneList):
    for i in range(len(oneList)):
        for j in range(len(oneList) - 1):
            if oneList[j] > oneList[j + 1]:
                buf = oneList[j + 1]
                oneList[j + 1] = oneList[j]
                oneList[j] = buf

def printList(oneList):
    for elem in oneList:
        print(elem, end=' ')
    print()

sortList(someList)
printList(someList)

numb = 0
col = 0
maxcol = 1
most_often_numb = 'Нету'
most_often_numb2 = "все"

while True:
	if numb == 101:
		print('Самое частое число :', most_often_numb,"и",most_often_numb2)
		break
	for elem in someList:
		if elem == numb:
			col += 1
	if col > maxcol:
		if maxcol == col:
			most_often_numb2 = most_often_numb
		maxcol = col
		most_often_numb = numb
	numb += 1
	col = 0