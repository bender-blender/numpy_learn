
#Булевы операции и функции, значения inf и nan

import numpy as np


#TODO Функции greater, less, equal


a = np.array([1,2,3,4])
b = np.array([5,6,7,8])

c = np.greater(a,b) #! Выполняет сравнение a > b

print(c) 

d = np.less(a,b) #! Выполняет сравнение a < b
print(d)

e = np.equal(a,b) #! Выполняет сравнение a == b
print(e)
#-------------------

#TODO array_equal, all и any.

f = np.array_equal(a,b) #! Выполняет сравнение массивов
print(f)

a = b
f = np.array_equal(a,b)
print(f)

print(a[a > 3]) #! Есть такой тип сортировки, он достаточно быстро работает, в отличии от циклов

print(np.any(a > 7)) #! Ищет, чтоб  хотя бы один элемент проходили условие 

print(np.all(a > 3)) #! Ищет, чтоб все элементы проходили условие 
#-------------------



# TODO Значения -inf, inf и nan.

print(a / 0)

d = a / 0
#! inf - представление (положительной) бесконечности с плавающей запятой
#! nan - не число 

print(d * 0)

#-------------------
#TODO Функции isnan и isinf.


#! Проверяет на наличие nan и isinf

i = np.isinf(d)
o = np.isnan(d)

print(i)
print(o)