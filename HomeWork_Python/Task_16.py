# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

# *Пример:*

# 5
#     1 2 3 4 5
#     3
#     -> 1

N = int(input('Enter the number of elements in the array: '))
enter_N = input('Enter the array elements (using a space between the numbers): ').split()
arr = list(map(int, enter_N))
if len(enter_N) != N or N == 0:
    print('Input error.')
else:
    X = int(input('Enter the desired number: '))
    count = 0
    for i in range(N):
        if arr[i] == X:
            count += 1
print(f'The number {X} occurs in the array A {count} times.')