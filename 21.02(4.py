a = input()
b = input()
if (a.lower() == 'красный' and b.lower() == 'синий') or (b.lower() == 'красный' and a.lower() == 'синий'):
    print('фиолетовый')
elif (a.lower() == 'красный' and b.lower() == 'желтый') or (b.lower() == 'красный' and a.lower() == 'желтый'):
    print('оранжевый')
elif (a.lower() == 'синий' and b.lower() == 'синий') or (b.lower() == 'синий' and a.lower() == 'желтый'):
    print('зеленый.')
else:
    print('Неверный цвет')
