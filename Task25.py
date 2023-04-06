# 25. Напишите программу, которая принимает на вход
# строку, и отслеживает, сколько раз каждый символ
# уже встречался. Количество повторов добавляется к
# символам с помощью постфикса формата _n.
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
# Для решения данной задачи используйте функцию .split()

sp = input('Введите строку: ').split()
result = {}
for i in sp:
    if i in result:
        print(f'{i}_{result[i]}')
    else:
        print(i, end='_1\n')
    result[i] = result.get(i, 1) + 1

# a = str(input("Введите строку: "))
# fantom_a = list()
# for el in a:
#     fantom_a.append(el)
#     print(f"{el}_{fantom_a.count(el)}")
