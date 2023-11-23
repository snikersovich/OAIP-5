#Задача 1
a = [int(input('')) for i in range(int(input()))]
print(len(set(''.join(map(str, a)))))

#Задача 2
a = set(input())
a2 = set(input())
a3 = set(input())
d1 = (a & a2)
d2 = (a2 & a3)
d3 = (a3 & a)
print(d1 | d2 | d3)

#Задача 3
num = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
a = input('Введите число: ')
print('Этих цифр не было')
print(set(num) - set(map(int, a)))

#Задача 4
number = []
num = int(input('Введите числа: '))
while num != 0:
    number.append(num)
    num = int(input('Введите числа: '))
count = len(number)
a = [num for num in number if num % count == 0]
print(a)

#Задача 5
n = int(input('Введите количество флагов: '))
flag = [input('Введите цвет: ') for i in range(n)]
a = int(input('Количество флагов в гирлянде: '))
d, a2 = divmod(a, n)
print(*(flag * d + flag[:a2]), sep='\n')

#Задача 6
years = {"Proterozoic": range(635 * 10 ** 6, 2800 * 10 ** 6),
         "Cenozoic": range(0, 145 * 10 ** 6),
         "Mesozoic": range(145 * 10 ** 6, 300 * 10 ** 6),
         "Paleozoic": range(300 * 10 ** 6, 635 * 10 ** 6)}
while True:
    x = input('Укажите год: ')
    if x == "":
        break
    x = int(x) * 1000
    for i, val in years.items():
        if x in val:
            print(i)
            break
    else:
        print("Archaea")

#Задача 7
a = [int(input('')) for i in range(int(input( )))]
print(len(set(''.join(map(str, a)))))

#Задача 8
a = input('')
le = [*map(bin, map(int, a.split()))]
s = [{'digits': len(w)-2, 'units': w.count('1'), 'zeros': w.count('0')-1}for w in le]
print(s)
