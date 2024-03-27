a = [5, 2, 6, 7, 3, 5]
d = []
u = []
for a in a:
    if a in u and a not in d:
        d.append(a)
    else:
        u.append(a)
if d:
    print('Есть повторы')
else:
    print('Повторов нет')