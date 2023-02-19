class Car:
    name = "2114"
    make = "lada"
    model = 2008

    # создаем методы класса
    def start(self):
        print("Заводим двигатель")

    def stop(self):
        print("Отключаем двигатель")
car_a= Car()
car_b= Car()
print(type(car_b))
car_b.start()
print(car_b.model)
print(dir(car_b))

class Car:
    car_count = 0
    def start(self, name, make, model):
        print("Двигатель заведен")
        self.name = name
        self.make = make
        self.model = model
        Car.car_count += 1

car_a1 = Car()
car_a1.start("Corrola", "Toyota", 2015)
print(car_a1.name)
print(car_a1.car_count)
car_b2 = Car()
car_b2.start("City", "Honda", 2013)
print(car_b2.name)
print(car_b2.car_count)

class Car:

    @staticmethod
    def get_class_details():
        print("Это класс Car")


Car.get_class_details()

class Car:

    def __str__(self):
        return "Car class Object"

    def start(self):
        print("Двигатель заведен")


car_a2 = Car()
print(car_a2)


class Car:
    car_count = 0
    def __init__(self):
        Car.car_count += 1
        print(Car.car_count)
car_a3 = Car()
car_b3 = Car()
car_c3 = Car()

class Vehicle:
    def vehicle_method(self):
        print("Это родительский метод из класса Vehicle")

class Car(Vehicle):
    def car_method(self):
        print("Это метод из дочернего класса")

car_a5 = Car()
car_a5.vehicle_method()