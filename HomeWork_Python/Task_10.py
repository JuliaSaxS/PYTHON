# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, 
# а некоторые – гербом. Определите минимальное число монеток, 
# которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. 
# Выведите минимальное количество монет, которые нужно перевернуть

n = int(input('Enter the number of coins: '))
heads = tails = 0
for i in range(n):
    x = int(input('If the coin is heads, enter 0, if tails, enter 1: '))
    if x == 0:
        heads += 1
    else:
        tails += 1
if heads < n/2:
    print(f'Coins need to be turned {heads} times.')
else:
    print(f'Coins need to be turned {tails} times.')