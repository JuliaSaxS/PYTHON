# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

n = int(input('Enter the number n: '))
x = 0
while 2 ** x <= n:
    print(2 ** x)
    x += 1
