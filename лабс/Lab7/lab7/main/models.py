from django.db import models
from django.forms import ModelForm

# Create your models here.


#Виды автомобилей
class CarType(models.Model):
    model = models.CharField('Модель', max_length=50)
    color = models.CharField('Цвет', max_length=50)
    price = models.IntegerField()

    names = ["Индекс", "Модель", "Цвет", "Цена"]
    title = "Виды автомобилей"

    def get_dict(self):
        return {"id": self.id, 0: self.model, 1: self.color, 2: self.price}

    def __str__(self):
        return str(self.id)


#Автомобили
class Car(models.Model):
    model_id = models.ForeignKey(CarType, on_delete=models.CASCADE)
    buy_location = models.CharField("Локация покупки", max_length=150)
    owner_FIO = models.CharField("ФИО владельца", max_length=150)

    names = ["Индекс", "Индекс модели", "Локация покупки", "Фио владельца"]
    title = "Автомобили"

    def get_dict(self):
        return {"id": self.id, 0: self.model_id, 1: self.buy_location, 2: self.owner_FIO}

    def __str__(self):
        return str(self.model_id)



#Проездная точка
class TravelPoint(models.Model):
    name = models.CharField("Название", max_length=150)
    main_owner_id = models.ManyToManyField('OwnerTravelPoint')

    names = ["Индекс", "Название", "Индекс главного владельца"]
    title = "Проездная точка"

    def get_dict(self):
        return {"id": self.id, 0: self.name, 1: ", ".join(map(str, self.main_owner_id.all()))}

    def __str__(self):
        return str(self.id)


#Владелец проездных точек
class OwnerTravelPoint(models.Model):
    FIO = models.CharField("ФИО", max_length=250)
    age = models.IntegerField()

    names = ["Индекс", "Фио", "Возраст"]
    title = "Владелец проездной точки"

    def get_dict(self):
        return {"id": self.id, 0: self.FIO, 1: self.age}


    def __str__(self):
        return str(self.id)


#История проездов автомобилей
class CarPass(models.Model):
    date_time = models.DateTimeField()
    plate_number = models.CharField("Номерной знак", max_length=150)
    car_id = models.ForeignKey('Car', on_delete=models.DO_NOTHING)
    travel_point_id = models.ForeignKey(TravelPoint, on_delete=models.DO_NOTHING)

    names = ["Номер", "Дата и время", "Номерной знак", "Индекс автомобиля", "Индекс проездной точки"]
    title = "История проезда автомобилей"

    def get_dict(self):
        return {"id": self.id, 0: self.date_time, 1: self.plate_number, 2: self.car_id, 3: self.travel_point_id}

    def __str__(self):
        return str(self.id)


#Характеристики проезжающих автомобилей
class DataOfPassingCar(models.Model):
    numberHistory = models.OneToOneField('CarPass', on_delete=models.CASCADE, primary_key=True)
    speed = models.FloatField()
    driverFIO = models.CharField("Фио водителя", max_length=250)

    names = ["Номер истории", "Скорость", "Фио владельца"]
    title = "Характеристика проезжающих автомобилей"

    def get_dict(self):
        return {"id": self.numberHistory, 0: self.speed, 1: self.driverFIO}

    def __str__(self):
        return str(self.id)



class Article(models.Model):
    title = models.CharField('Название', max_length=50)
    anons = models.CharField('Анонс', max_length=250)
    full_text = models.TextField('Статья')
    date = models.DateTimeField('Дата публикации')

    def __str__(self):
        return self.title