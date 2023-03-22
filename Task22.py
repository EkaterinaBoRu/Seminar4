"""Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств."""

n = int(input("Введите число элементов первого множества: "))
m = int(input("Введите число элементов второго множества: "))

n_list = tuple()
m_list = tuple()
k_list = tuple()


print("Введите числа первого множеста:")
n_list = [tuple(map(int, input().split())) for i in range(n)]

print("Введите числа второго множеста:")
m_list = [tuple(map(int, input().split())) for i in range(m)]

#if n_list[i] == m_list[0] for i in n_list

"""if n_list== m_list:
    print (n_list)"""

for i in range(n):
    for j in range(m):
        if n_list[i]== m_list[j]:
            k_list = k_list + n_list[i]

print(sorted(k_list))