words = []
while True:
    word = input('Введите слово')
    if word.lower() == 'stop':
        break
    words.append(word)
    print('')
results = ' '.join(words)
print(results)