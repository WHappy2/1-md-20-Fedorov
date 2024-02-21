a = int(input('Введите номер места'))
if a < 1 or a > 40:
    print('неверный номер')
else:
    if a % 2 == 0:
        print('Верхнее место')
    else:
        print('Нижнее место')
    if a <= 32:
        print('купе')
    else:
        print('боковое')