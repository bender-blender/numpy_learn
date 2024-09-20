#Свойства и представления массивов, создание их копий
import numpy as np

#TODO Свойство

a = np.array([1,2,3,4,5])
# У каждого массива есть размер и тип элементов

a.dtype = "int8"
print(a)

print(a.size) # Можно вывести размер массива
print(a.itemsize) # Размер элемента в байтах

print(a.ndim) # Число осей

a = np.array([[1,2,3],[4,5,6]])
print(a.ndim)

print(a.shape) # Размерность массива 

#TODO Копирование

b = a.view() 
a[0] = 100 
print(a) 
print(b) 