# Задача 2: Найдите сумму цифр трехзначного числа.

# *Пример:*

# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) 

# ver. 1

# a = int(input('Enter a three-digit number: '))
# if(a >= 100 and a <= 999):
#     sum = (a // 100) + (a // 10 % 10) + (a - (a // 10) * 10)
#     print(f'The sum of all digits of the number {a} is equal to {sum}.')
# else:
#     print('Input error.')
    
# ver. 2

a = input('Enter a three-digit number: ')
sum = int(a[0]) + int(a[1]) + int(a[2])
print(f'The sum of all digits of the number {a} is equal to {sum}.')
