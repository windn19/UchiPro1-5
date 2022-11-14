class Pets:
    def __init__(self, name, male, fury):
        self.name = name
        self.male = male
        self.fury = fury

    def eat(self, weight):
        print(f'{self.name} съел {weight} корма')

    def __str__(self):
        return f'Питомец {self.name} {self.male} пола c {self.fury} шестью'


class Dog(Pets):
    def __init__(self, name, male, fury, weight):
        super().__init__(name, male, fury)
        self.weight = weight

    def walk(self, min):
        print(f'Собачка {self.name} погулял {min} минут')


class Cat(Pets):
    def sleep(self, min):
        print(f'Котик {self.name} поспал {min} минут')


if __name__ == '__main__':
    cat = Pets('Васька', "мужского", "короткошерстный")
    print(cat)
    cat.eat(12)
    cat2 = Cat('Петька', 'женского', 'длинношерстный')
    print(hasattr(cat, 'sleep'))
    print(cat2)
    cat2.sleep(20)
    dog = Dog('Шарик', 'мужской', 'короткошерстный', 10)
    print(dog)
    dog.walk(10)
    print(dog.weight)
    print(cat2)

