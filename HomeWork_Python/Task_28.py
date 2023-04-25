# Задача 28: Напишите рекурсивную функцию sum(a, b), 
# возвращающую сумму двух целых неотрицательных чисел. 
# Из всех арифметических операций допускаются только +1 и -1. 
# Также нельзя использовать циклы.

# *Пример:*

# 2 2
#     4 

a = int(input('Enter the first number: '))
b = int(input('Enter the second number: '))
def sum(a, b):
    if a == 0:
        return b
    else:
        return sum(a - 1, b + 1)
print(f'{a} + {b} = {sum(a, b)}')