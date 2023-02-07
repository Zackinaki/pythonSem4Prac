# 1. Даны два неупорядоченных набора целых чисел (может быть, с повторениями). Выдать без повторений
#  в порядке возрастания все те числа, которые
# встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во элементов второго
#  множества. Затем пользователь вводит сами элементы множеств

# Пример:
# 11 6
# 2 4 6 8 10 12 10 8 6 4 2
# 3 6 9 12 15 18

# 6 12

import os
os.system('cls')

n = int(input("Vvdedite kol-vo elementov v mnozhestve 1: "))
m = int(input("Vvdedite kol-vo elementov v mnozhestve 2: "))
print("Vvedite znachenia mnozhesta 1: ")
a = {input() for i in range(n)}
print("Vvedite znachenia mnozhesta 2: ")
b = {input() for i in range(m)}

c = a.intersection(b)
d = list(c)

print("Chisla vstrechaushiesa v oboih mnozhestvah v poradke vozrastania", d)
