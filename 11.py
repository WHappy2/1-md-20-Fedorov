class Restaurant:
    def __init__(self, restaurant_name, cuisine_type, rating=0):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.rating = rating

    def describe_restaurant(self):
        print(f"Название ресторана: {self.restaurant_name}")
        print(f"Тип кухни: {self.cuisine_type}")
        print(f"Рейтинг ресторана: {self.rating}")

    def open_restaurant(self):
        print(f"Ресторан {self.restaurant_name} открыт!")

    def set_rating(self, new_rating):
        self.rating = new_rating
        print(f"Рейтинг ресторана {self.restaurant_name} обновлен до {self.rating}")

# Создание экземпляра класса Restaurant
newRestaurant = Restaurant("La Bella", "Итальянская кухня")
newRestaurant.describe_restaurant()
newRestaurant.open_restaurant()

# Создание трех разных экземпляров класса Restaurant
restaurant1 = Restaurant("Peking Duck", "Китайская кухня")
restaurant2 = Restaurant("Sushi Bar", "Японская кухня")
restaurant3 = Restaurant("Burger King", "Фастфуд")

# Вызов метода describe_restaurant() для каждого экземпляра
restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()

# Обновление рейтинга
newRestaurant.set_rating(5)
restaurant1.set_rating(4)
restaurant2.set_rating(4.5)
restaurant3.set_rating(3.5)
