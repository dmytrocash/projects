a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

# Выведите все элементы, которые меньше 5 в списке а.

for x in a:
    if x < 5:
        print(x)

# Верните список, который состоит из элементов, общих для этих двух списков.

c = []

for y in a:
   if y in b:
       c.append(y)

print(c)

# Отсортируйте полученный список по убыванию.

c.sort(reverse=True)
print(c)

# Напишите программу для слияния списков a и b
ab = []

for z in a:
    ab.append(z)
for z in b:
    ab.append(z)

print(ab)

# Сформируйте новый возрастающий список из чётных чисел (количество элементов в списке - 45)

newlist = []  

for i in range(90):

   if i % 2 == 0:

       newlist.append(i)

print(len(newlist))
print(newlist)
