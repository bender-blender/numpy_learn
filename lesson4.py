
#TODO Изменение формы массивов, добавление и удаление осей
import numpy as np

a = np.arange(0,32)
print(a)

a.shape = 4,8 #TODO Изменение формы
print(a)


b = np.array([[1,2,3,4],[5,6,7,8]])
b.reshape(-1,2) #TODO используется для преобразования одномерного массива в двумерный
print(b) 

y = np.ravel(b) #TODO разлаживает матрицы в вектор
print(y)



c = np.array([[1,2,3],[4,5,6]])
d = np.resize(c,(2,8))
print(d)
"""
Если новый массив больше исходного, то новый массив заполняется повторяющимися копиями 
a. Обратите внимание, что это поведение отличается от поведения a.resize(new_shape),
которое заполняется нулями вместо повторяющихся копий a.
"""


print(c.T) #TODO транспонирования матриц



a = np.arange(0,10)
print(a)
b = np.expand_dims(a,0) #TODO добавляет ось
print(b)


d = np.squeeze(a) #TODO удалить ось
print(d)