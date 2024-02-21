a = int(input())
if (a % 2 == 0 and a%100 != 0) and (a%400 == 0):
    print('Высокосный')
else:
    print('обычный')
