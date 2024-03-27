days = ('Пн','Вт','Ср','Чт','Пт','Сб','Вс')
h = int(input('Сколько выходных вы хотите'))
print('У вас выходных', h)
wi = range(-h,0)
wl = []
wrl = []
for i in wi:
    wl.append((days[i]))
for day in days:
    if day not in wl:
        wrl.append((day))
print('выходные')
print('\n'.join(wl))
print('рабочие')
print('\n'.join(wrl))