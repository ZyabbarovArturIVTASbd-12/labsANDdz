#Полиморфизм - способность обьекта использовать методы производного класса, который не существует на момент создания базового
#В данной программе мы не создавали общего родительского класса
#Даже если мы можем упаковать два разных объекта в кортеж и итерировать по нему, мы будем использовать общую переменную people. Это возможно благодаря полиморфизму.

class Man:
    def __init__(self, name, univer, age):
        self.name = name
        self.univer = univer
        self.age = age

    def infa(self):
        print(f"Всем прив! Меня зовут {self.name}, мне {self.age} лет. Я учусь в {self.univer}.")

    def prikol(self):
        print("poop")


class Girl:
    def __init__(self, name, univer, age):
        self.name = name
        self.univer = univer
        self.age = age

    def infa(self):
        print(f"Всем приветик! Меня зовут {self.name}, мне {self.age} лет. Я учусь в {self.univer}.")

    def prikol(self):
        print("poopee")

malchik = Man("Артур", "Улгту", 19)
devka = Girl("Маша", "Улгу", 22)

for people in (malchik, devka):
    people.prikol()
    people.infa()
    people.prikol()

