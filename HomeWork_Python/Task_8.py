# Задача 8: Требуется определить, можно ли от шоколадки размером 
# n × m долек отломить k долек, если разрешается сделать один разлом 
# по прямой между дольками (то есть разломить шоколадку на два прямоугольника).

# *Пример:*

# 3 2 4 -> yes
# 3 2 1 -> no

n = int(input('Enter the number of chocolate slices in length: '))
m = int(input('Enter the number of chocolate slices in width: '))
k = int(input('How many slices of chocolate do you need to break off: '))
if k < n * m and ((k % n == 0) or (k % m == 0)):
    print('Yes')
else:
    print('No')