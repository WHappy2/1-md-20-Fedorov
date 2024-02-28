import random
point=0
errors = 0
while errors < 3:
    num1 = random.randint(1,10)
    num2 = random.randint(1,10)
    operation = random.choice(['+' , '-'])
    if operation == '+':
        result= num1 + num2
    else:
        result = num1 - num2
    answer = input(f'Сколько будет{num1} {operation} {num2}').lower()

    if answer == 'stop':
        break

    elif int(answer)!= result:
        errors +=1
        print('Вы допустили ошибку')

    else:
        print('Правильно')
        point += 1


if errors >=3:
    print('Игра окончена. Вы допустили игра окончена')
else:
    print('Игра окончена. Правильных ответов',point)