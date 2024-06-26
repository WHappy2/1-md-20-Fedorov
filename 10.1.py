import json

# Считывание информации из файла JSON
with open('1.json', 'r', encoding='utf-8') as file:
    a = json.load(file)

# добавляем продукт
main_product = {
    "name": input("Введите название продукта: "),
    "price": int(input("Введите цену продукта: ")),
    "available": input("Продукт в наличии? (да/нет): ").lower() == 'да',
    "weight": int(input("Введите вес продукта: "))
}
a['products'].append(main_product)

with open('products.json', 'w', encoding='utf-8') as file:
    json.dump(a, file, ensure_ascii=False, indent=4)


for product in a['products']:
    print(f"Название: {product['name']}")
    print(f"Цена: {product['price']}")
    print(f"Вес: {product['weight']}")
    if product['available']:
        print("В наличии")
    else:
        print("Нет в наличии!")