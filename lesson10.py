
#TODO Множества (unique) и операции над ними

import numpy as np
#! Множество, это массив с уникальными значениями

a = np.array([1,2,3,4,1,2,3,4])
b = np.unique(a) #TODO превратить массив в множество
print(b)

#! Можно возвращать элементы, которые повторяются
#! Их индексы , а также можно выполнить операцию unique 

b = np.unique(a,return_counts=True)
print(b)

b = np.unique(a,return_index=True)
print(b)


a = np.array([1,2,3,4,1,2,3,4])
b = np.array([1,5,1,6,1,2,4,1])
print(np.intersect1d(a,b)) # Пересечение
print(np.union1d(a,b)) # Объединение
print(np.setdiff1d(a,b)) # Вычитание
print(np.setxor1d(a,b)) # Симметрическая разность