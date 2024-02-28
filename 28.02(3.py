
while True:
    word = input('Введите слово:').lower()
    if 'ф' in word:
        print('Ого! Это редкое слово!', word)
        break
    else:
        print('Эх, это не очень редкое слово...', word)

