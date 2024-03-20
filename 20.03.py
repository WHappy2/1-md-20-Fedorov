def a(b):
    if b % 5 ==0:
        return True
    else:
        return False
b = int(input())
if a(b):
    print(b,'Делиться на 5')
else:
    print(b,'Не делиться на 5')

def a2():
    try:
        b = int(input())
        result = 300/b
        print(result)
    except ValueError:
        print('Ошибка:введено не полное число')
    except ZeroDivisionError:
        print('Ошибка:на 0 делить нельзя')
a2()

def a3(date):
    try:
        day,month,year = map(int,date.split('/'))
        if day*month == year % 100:
            return True
        else:
            return False
    except ValueError:
        return False
date = input('Введите дату')
if a3(date):
    print('Магичекая дата')
else:
    print('Немагическая дата')

def a4(luck):
    tnumber=str(luck)
    if len(luck) % 2 != 0:
        return False
    hl = len(luck) // 2
    fhs = 0
    sfs = 0
    for i in range(hl):
        fhs += int(luck[i])
        sfs += int(luck[i])
    return fhs == sfs
luck=input('Введите номер билета')
if a4(luck):
    print('Это счастливый билет')
else:
    print('Это не счастливый билет')