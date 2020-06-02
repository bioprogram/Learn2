# 9.1. Ресторан: создайте класс с именем Restaurant . Метод __init__() класса Restaurant
# должен содержать два атрибута : restaurant_name и cuisine_type . Создайте метод describe_
# restaurant() , который выводит два атрибута, и метод open_restaurant() , который выводит
# сообщение о том, что ресторан открыт.
# Создайте на основе своего класса экземпляр с именем restaurant . Выведите два атрибута
# по отдельности, затем вызовите оба метода.

class Restaurant():
    """A class representing a restaurant."""

    def __init__(self, name, cuisine_type):
        """Initialize the restaurant."""
        self.name = name.title()
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Display a summary of the restaurant."""
        msg = f"{self.name} serves wonderful {self.cuisine_type}."
        print(f"\n{msg}")

    def open_restaurant(self):
        """Display a message that the restaurant is open."""
        msg = f"{self.name} is open. Come on in!"
        print(f"\n{msg}")

mean_queen = Restaurant('the mean queen', 'pizza')
mean_queen.describe_restaurant()

ludvigs = Restaurant("ludvig's bistro", 'seafood')
ludvigs.open_restaurant()

mango_thai = Restaurant('mango thai', 'thai food')
mango_thai.describe_restaurant()