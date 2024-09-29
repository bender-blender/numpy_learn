
#TODO Базовые математические функции 

import numpy as np

a = np.arange(0,10)

print(a.sum()) #! Сумма 

print(a.max()) #! Максимальное значение

print(a.min()) #! Минимальное значение(Также при необходимости можно указать ось)


print(a.mean()) #! Вычислить среднее значение

#--------------------

#TODO Тригонометрические функции

b = np.array([1,2,3,4,5,6])
print(np.sin(b)) #! Синус

print(np.cos(b)) #! Косинус


#--------------------

#TODO Функции генерации псевдослучайных чисел

c = np.random.rand() #! Генерирует числа не больше 1
print(c)




b = np.random.randint(0,20,size=20).reshape(4,5) #! Генерирует случайное число в диапазоне, можно указать размер массива
print(b)


e = np.random.seed(13) #! Установка начального генератора

b = np.random.randint(0,20,size=20).reshape(4,5)
print(b)

#--------------------

#TODO Функции перемешивания значений

b = np.random.randint(0,20,size=20)
print(b)
np.random.shuffle(b)
print(b)

e = np.random.permutation(10)
print(e)