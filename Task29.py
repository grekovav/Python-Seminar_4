# 29. Ваня и Петя поспорили, кто быстрее решит
# следующую задачу: “Задана последовательность
# неотрицательных целых чисел. Требуется определить
# значение наибольшего элемента
# последовательности, которая завершается первым
# встретившимся нулем (число 0 не входит в
# последовательность)”. Однако 2 друга оказались не
# такими смышлеными. Никто из ребят не смог до
# конца сделать это задание. Они решили так: у кого
# будет меньше ошибок в коде, тот и выиграл спор. За
# помощью товарищи обратились к Вам, студентам.

# # Ваня:
# n = int(input())
# max_number = 1000
# while n != 0:
#     n = int(input())
# if max_number > n:
#     max_number = n
# print(max_number)

# # Петя:
# n = int(input())
# max_number = -1
# while n < 0:
#     n = int(input())
# if max_number < n:
#     n = max_number
# print(n)

a = [2, 3, 4, 5, 6, 7, 3, 11, 0, 19, 5]
max = a[0]
for el in a:
    if el > max:
        max = el
    if el == 0:
        break
print(max)