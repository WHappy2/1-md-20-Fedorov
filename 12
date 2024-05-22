class Restaurant:
    def __init__(self, restaurant_name, cuisine_type, rating=0):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.rating = rating

    def describe_restaurant(self):
        print(f"Название ресторана: {self.restaurant_name}")
        print(f"Тип кухни: {self.cuisine_type}")
        print(f"Рейтинг: {self.rating}")

    def open_restaurant(self):
        print(f"Ресторан {self.restaurant_name} сейчас открыт!")

    def set_rating(self, new_rating):
        self.rating = new_rating
        print(f"Новый рейтинг ресторана {self.restaurant_name}: {self.rating}")

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type, flavors, location='', hours=''):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors
        self.location = location
        self.hours = hours

    def show_flavors(self):
        print(f"У нас есть следующие вкусы мороженого: {', '.join(self.flavors)}")

    def add_flavor(self, flavor):
        self.flavors.append(flavor)
        print(f"Вкус {flavor} добавлен в список.")

    def remove_flavor(self, flavor):
        if flavor in self.flavors:
            self.flavors.remove(flavor)
            print(f"Вкус {flavor} удален из списка.")
        else:
            print(f"Вкус {flavor} не найден в списке.")

    def check_flavor(self, flavor):
        return flavor in self.flavors

# Создание экземпляра класса Restaurant
newRestaurant = Restaurant("Великолепный ресторан", "Итальянская кухня")
newRestaurant.describe_restaurant()
newRestaurant.open_restaurant()

# Создание трех разных экземпляров класса Restaurant
restaurant1 = Restaurant("Рай Пасты", "Итальянская кухня")
restaurant2 = Restaurant("Мир Суши", "Японская кухня")
restaurant3 = Restaurant("Уголок Карри", "Индийская кухня")

# Вызов метода describe_restaurant() для каждого экземпляра
restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()

# Создание экземпляра класса IceCreamStand
ice_cream_stand = IceCreamStand("Ледяные Удовольствия", "Десерты", ["Ваниль", "Шоколад", "Клубника"])
ice_cream_stand.show_flavors()

# Добавление и удаление вкусов мороженого
ice_cream_stand.add_flavor("Мята")
ice_cream_stand.remove_flavor("Ваниль")
ice_cream_stand.show_flavors()

# Проверка наличия вкуса мороженого
if ice_cream_stand.check_flavor("Шоколад"):
    print("Вкус шоколад доступен!")
else:
    print("Вкус шоколад не доступен!")
