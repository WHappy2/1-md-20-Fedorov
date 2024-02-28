a = int(input('Введите количество слов:'))
words = []
for i in range(a):
    word = input('Введите слово')
    words.append(word)
results = ''.join(words)
print(results)
