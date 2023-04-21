# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X.

# *Пример:*

# 5
#     1 2 3 4 5
#     6
#     -> 5

N = int(input('Enter the number of elements in the array: '))
enter_N = input('Enter the array elements (using a space between the numbers): ').split()
arr = list(map(int, enter_N))
if len(enter_N) != N or N == 0:
    print('Input error.')
else:
    X = int(input('Enter the desired number: '))
    index = 0
    min = abs(X - arr[0])
    for i in range(1, N):
        count = abs(X - arr[i])
        if count < min:
            min = count
            index = i
    print(f"The closest element in size to the number {X} is {arr[index]}.")
