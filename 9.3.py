import csv

# Считывание данных из файла CSV
total_stoimost = 0
with open('1.csv', 'r', newline='', encoding='windows-1251') as file:
    # Указываем правильный разделитель, если он отличается от запятой
    read = csv.reader(file, delimiter=';')  # предполагаем, что разделитель - точка с запятой
    next(read)  # пропускаем заголовок
    print("Нужно купить:")
    for row in read:
            product, quantity, price = row
            stoimost = int(quantity) * int(price)
            print(f"{product} - {quantity} шт. за {price} руб.")
            total_stoimost += stoimost


# Вывод итоговой суммы
print(f"Итоговая сумма: {total_stoimost} руб.")