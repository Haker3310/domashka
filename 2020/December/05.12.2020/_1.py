import random
x = random.randint(5,15)
someList = [random.randint(0, 20) for i in range(random.randint(1,x))]
mx = someList[0] + someList[1] + someList[2] # делаем максимальной сумму первых трех эл-в
for i in range(3, x-2):
    s = someList[i] + someList[i+1] + someList[i+2] # ищем сумму следующих трех эл-в
    if s > mx: # cравниваем ее с предыдущим максимумом и т.д.
        mx = s # после того, как нашли конечный максимум
print(mx) # вывод конечного массива