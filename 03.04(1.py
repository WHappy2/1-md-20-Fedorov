cc = {'Россия':'Москва','Германия':'Берлин','Франция':'Париж','Италия':'Рим'}
print('пара страна-столица')
for country, capital in cc.items():
    print(country, capital)
country  = 'Россия'
print(f'Столица {country}',cc.get(country))
scc = dict(sorted(cc.items()))
print('Словарь в алфовитном порядке')
for country, capital in scc.items():
    print(country,capital)