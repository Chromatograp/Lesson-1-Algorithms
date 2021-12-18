print('Задание 8.')

# 8. Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).

a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
c = int(input('Введите третье число: '))

if a > c and a < b or a < c and a > b:
    print(a)
elif b < c and b > a or b > c and b < a:
    print(b)
elif c < a and c > b or c > a and c < b:
    print(c)