# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. 
# n — кол-во элементов первого множества. m — кол-во элементов второго множества. 
# Затем пользователь вводит сами элементы множеств.

n = int(input('Enter the number of elements of the first set: '))
m = int(input('Enter the number of elements of the second set: '))
first_set = []
second_set = []
result_set = []
for i in range(n):
    first_set.append(int(input('Enter elements of the first set: ')))
for i in range(m):
    second_set.append(int(input('Enter elements of the second set: ')))
for i in first_set:
    if i in second_set and i not in result_set:
        result_set.append(i)
result_set.sort()
print(first_set)
print(second_set)
print(result_set)