# Задача №9.
# По данному целому неотрицательному n вычислите
# значение n!. N! = 1 * 2 * 3 * … * N (произведение всех
# чисел от 1 до N) 0! = 1 Решить задачу используя цикл while
# Input: 5
# Output: 120

# ver. 1:
# 
# def factorial(n: int) -> int:
#     result = 1
#     i = 1
#     while i <= n:
#         result *= i
#         i += 1
#     return result
# number = int(input('Enter the number: '))
# print(factorial(number))

# ver. 2:

# number = int(input('Enter the limit: '))
# fact = 1
# i = 1
# while i <= number:
#     fact *= i
#     i += 1
# print(fact)    

# ver. 3:

# number = int(input('Enter the limit: '))
# fact = 1
# for i in range(1, number + 1):      # range(start, finish, step)
#     fact *= i
# print(fact)
    
# for i in range(10):
#     print(i)
# print(i)

# Задача №11.
# Дано натуральное число A > 1. Определите, каким по
# счету числом Фибоначчи оно является, то есть
# выведите такое число n, что φ(n)=A. Если А не
# является числом Фибоначчи, выведите число -1.
# Input: 5
# Output: 6

# ver. 1:

# number = int(input('Enter the number you want to check: '))
# count_of_fibonacci_number = 2
# first_previous_fibonacci_number = 0
# second_previous_fibonacci_number = 1
# current_fibonacci_number = 0
# while current_fibonacci_number <= number:
#     current_fibonacci_number = first_previous_fibonacci_number + second_previous_fibonacci_number
#     first_previous_fibonacci_number = second_previous_fibonacci_number
#     second_previous_fibonacci_number = current_fibonacci_number
#     count_of_fibonacci_number += 1
#     if (current_fibonacci_number == number):
#         print(count_of_fibonacci_number) 
#         exit(0)
# print(-1)    
    
# ver. 2:

# A = int(input("Введите число: "))
# f1 = 0
# f2 = 1
# count = 2
# while f2 < A:
#     f3 = f1 + f2
#     f1 = f2
#     f2 = f3
#     count += 1
# if f2 == A:
#     print("Порядковый номер по Фибоначчи", count)
# else:
#     print("-1")    

# ver. 3:

# a = int(input('Enter the number you want to check: '))
# i = 2
# first = 0
# second = 1
# while i <= a:
#     fibonacci = first + second
#     first = second
#     second = fibonacci
#     i += 1
#     if (fibonacci == a):
#         print(i) 

# ver. 4:

# number = int(input('Enter the number you want to check: '))
# first = 0
# second = 1
# index = 1
# while second < number:
#     first, second = second, first + second
#     index += 1
# print(index if second == number else -1)

# my_list = [1, 2, 3, 4]
# print(my_list[::-1])          # разворот массива

# a = 5
# b = 10
# c = 15
# print(a)
# print(b)
# print(c)
# a, b, c = c, b, a
# print(a)
# print(b)
# print(c)                # разворот последовательности

# Задача №13. 
# Уставшие от необычно теплой зимы, жители решили узнать,действительно ли это самая длинная оттепель за всю историю
# наблюдений за погодой. Они обратились к синоптикам, а те, в свою очередь, занялись исследованиями статистики за
# прошлые годы. Их интересует, сколько дней длилась самая длинная оттепель. Оттепелью они называют период, в
# который среднесуточная температура ежедневно превышала 0 градусов Цельсия. Напишите программу, помогающую
# синоптикам в работе.Пользователь вводит число N – общее количество рассматриваемых дней (1 ≤ N ≤ 100). В следующих строках
# располагается N целых чисел.
# Каждое число – среднесуточная температура в
# соответствующий день. Температуры – целые числа и лежат в
# диапазоне от –50 до 50
# Input: 6 -> -20 30 -40 50 10 -10
# Output: 2

# ver. 1:

# import random
# all_days = int(input('Enter the number of days: '))
# today = 0
# i = 1
# count = 0
# max = 0
# while i <= all_days:
#     today += random.randint(-3, 3)
#     print(today, end=" ")        
#     if today > 0:
#         count += 1
#         if max < count:
#             max = count
#     else:
#         count = 0
#     i += 1
# print(f"\n\n{max}")           

# ver 2:

# import random
# days = []
# today = 0
# counter = 0
# max = 0
# for i in range(1, 30):
#     today = random.randint(-3, 3)
#     days.append(today)
   
#     if today > 0:
#         counter += 1
#         if counter > max:
#             max = counter
#     else:
#         counter = 0
# print(days)
# print(counter)

# ver. 3:

# import random
# days = int(input('Enter the number of days: '))
# temp_max = 0
# temp_new_max = 0
# for i in range(days):
#     day_temp = random.randint(-50, 50)
#     print(f"{day_temp}", end=' ')
#     if day_temp > 0:
#         temp_new_max += 1
#         if temp_new_max > temp_max:
#             temp_max = temp_new_max
#     else:
#         temp_new_max = 0
# print(f'\nLongest thaw (consecutive days): {temp_max}')

# Задача №15. 
# Иван Васильевич пришел на рынок и решил купить два арбуза: один для себя, а другой для тещи.
# Понятно, что для себя нужно выбрать арбуз потяжелей, а для тещи - полегче. Но вот незадача:
# арбузов слишком много, и он не знает, как же выбрать самый легкий и самый тяжелый арбуз? Помогите ему!
# Пользователь вводит одно число N – количество арбузов. Вторая строка содержит N чисел,
# записанных на новой строчке каждое. Здесь каждое число – это масса соответствующего арбуза.
# Input: 5 -> 5 1 6 5 9
# Output: 1 9

# ver. 1:

# import random
# count = int(input('Enter the total number of watermelons: '))
# min = 30000
# max = 1
# for i in range(count):
#     weight = random.randint(1, 30000)
#     print(f'Weight of {i + 1} watermelon equal to {weight}.')
#     if weight > max:
#         max = weight
#     if weight < min:
#         min = weight
# print(f'\nFor yourself: {max}.\nFor mother-in-law: {min}.')

# ver. 2:

# import random
# count = int(input('Enter the total number of watermelons: '))
# min = 30000
# max = 1
# for i in range(count):
#     weight = random.randint(1, 30000)
#     print(weight, end=' ')
#     if weight > max:
#         max = weight
#     if weight < min:
#         min = weight
# print(f'\nFor yourself: {max}.\nFor mother-in-law: {min}.')

# ver. 3:

# import random
# num = int(input('Enter the total number of watermelons: '))
# watermelons = []
# for i in range(num):
#     watermelons.append(random.randint(1, 12))
# max = watermelons[0]
# min = watermelons[0]
# for i in range(num):
#     if watermelons[i] > max:
#         max = watermelons[i]
#     if watermelons[i] < min:
#         min = watermelons[i]
# print(watermelons)
# print(f'\nMin weigt of watermelon equal to {min}.\nMax weigt of watermelon equal to {max}.')

# ver. 4:

import random
n = int(input('Enter the total number of watermelons: '))
max = -1
min = 30001
for k in range(n):
    x = random.randint(-1, 30001)
    if x < min:
        min = x
    if x > max:
        max = x
print(max, min)

