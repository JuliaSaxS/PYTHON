# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. 
# Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), 
# а Катя должна их отгадать. 
# Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P. 
# Помогите Кате отгадать задуманные Петей числа.

print('Think of two numbers from 1 to 1000.')
S = int(input('Enter the sum of the planned numbers: '))
P = int(input('Enter the result of multiplication of the planned numbers: '))
if S < 1 or P < 1:
    print('Input error.')
for x in range(1001):
    for y in range(1001):
        if x + y == S and x * y == P:
            print(f'The intended numbers are {x} and {y}.')
            