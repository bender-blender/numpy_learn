
# Основные типы данных. Создание массивов функцией array() 
import numpy as np

a = np.array([1,2,3,4,5]) 
print(a)
#! Функция array принимает на вход обязательный параметр (объект)
#! И его тип (необязательный) и создает массив
c = np.float32(a)
print(c)

#TODO чем то похож на списки в Python, только более гибкий
print(c[0])

#! Также массив может хранить в себе объекты одного типа
#! По умолчанию, в таких ситуация все элементы превращаются в строки 
b = np.array((True,False,"12",3.14))
print(b)

#TODO Если надо сразу изменять элементы, dtype!
d = np.array((True,False,"12",3.14),dtype="int64")
print(d)
#! Также, нужно помнить о работе с памятью
#! Чем больше цифра в префиксе dtype - тем больше она может уместить данных
#! Но и расход памяти больше

print(b.__sizeof__())
print(d.__sizeof__())