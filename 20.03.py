def Zadanya1(ba):
    if ba % 5 ==0:
        result = ba,'Делиться на 5'
    else:
        result = ba,'Не делиться на 5'
    return result

def Zadanya2():
    try:
        b = int(input())
        result = 300/b
        print(result)
    except ValueError:
        print('Ошибка:введено не полное число')
    except ZeroDivisionError:
        print('Ошибка:на 0 делить нельзя')


def Zadanya3():
    def a(date):
        try:
            day, month, year = map(int, date.split('/'))
            if day+month >= year % 100:
                return True
            else:
                return False
        except ValueError:
            return False
        except MagicError as e:
            print(e)

    date = input('Введите дату')
    if a(date):
        print('Магическая')
    else:
        print('Немагическая')


def Zadanya4():
    def a(luck):

        tiket_number=str(luck)
        if len(luck) % 2 != 0:
            return False
        hl = len(luck) // 2
        fhs = 0
        shs = 0
        for i in range(hl):
            fhs += int(luck[i])
            shs += int(luck[i])
        return fhs == shs

    luck = input('Введите номер билета')
    if a(luck):
        print('')
    else:
        print('')

task = int(input('Введите номер задания'))
if task == 1:
    print(Zadanya1(int(input())))
elif task == 2:
    Zadanya2()
elif task ==3:
    print(Zadanya3())
elif task == 4:
    Zadanya4()
else:
    print('Такого нет')


