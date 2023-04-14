# За день машина проезжает n километров. Сколько дней нужно, чтобы проехать маршрут длиной m километров? 
# При решении этой задачи нельзя пользоваться условной инструкцией if и циклами.
# Input:
# n = 700
# m = 750
# Output:
# 2

# n = int(input('Enter how many kilometers the car drove in a day: '))
# m = int(input('Enter how many kilometers the car should travel in total: '))
# result = (m + n -1) // n
# print("The car drove %d kilometers in %d days"%(m, result))

# day = int(input('Enter how many kilometers the car drove in a day: '))
# total = int(input('Enter how many kilometers the car should travel in total: '))
# result = (day - 1 + total) // day
# print(f"The car drove {total} kilometers in {result} days.")

# import math
# n = 700 
# m = 750
# print(math.ceil(m//n))

# В некоторой школе решили набрать три новых
# математических класса и оборудовать кабинеты для
# них новыми партами. За каждой партой может сидеть
# два учащихся. Известно количество учащихся в
# каждом из трех классов. Выведите наименьшее
# число парт, которое нужно приобрести для них.
# Input: 20 21 22(ввод чисел НЕ в одну строку)
# Output: 32

# a = int(input('Enter the number of students in the first class: '))
# b = int(input('Enter the number of students in the second class: '))
# c = int(input('Enter the number of students in the third class: '))
# print(f'Need to buy {(a // 2 + a % 2) + (b // 2 + b % 2) + (c // 2 + c % 2)} desks')

# a = int(input())
# b = int(input())
# c = int(input())
# d = 2
# cls1 = a // d + a % 2
# cls2 = b // d + b % 2
# cls3 = c // d + c % 2
# res = (cls1 + cls2 + cls3)
# print(res)

# Вагоны в электричке пронумерованы натуральными
# числами, начиная с 1 (при этом иногда вагоны
# нумеруются от «головы» поезда, а иногда – с
# «хвоста»; это зависит от того, в какую сторону едет
# электричка). В каждом вагоне написан его номер.
# Витя сел в i-й вагон от головы поезда и обнаружил,
# что его вагон имеет номер j. Он хочет определить,
# сколько всего вагонов в электричке. Напишите
# программу, которая будет это делать или сообщать,
# что без дополнительной информации это сделать
# невозможно.
# Input: 3 4(ввод на разных строках)
# Output: 6

# i = int(input('Enter the number of the car in which the person boarded: '))
# j = int(input('Enter the number of the car in which the person was: '))
# if i == j: 
#     print('Without additional information, the definition is impossible.')
# else:
#     print(f'There are only {i + j - 1} cars on the train.')

# Дано натуральное число. Требуется определить,
# является ли год с данным номером високосным. Если
# год является високосным, то выведите YES, иначе
# выведите NO. Напомним, что в соответствии с
# григорианским календарем, год является
# високосным, если его номер кратен 4, но не кратен
# 100, а также если он кратен 400.
# Input: 2016
# Output: YES

year = int(input('Enter the year to check: '))
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print('Yes')
else:
    print('No')













