from django.db import models

# Create your models here.
class Product(models.Model):
    ID = models.BigAutoField(primary_key=True)
    owner = models.CharField(max_length=30)
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name
class Access(models.Model):
    product = models.ForeignKey('Product',on_delete=models.PROTECT)
    userID = models.IntegerField()

class Lesson(models.Model):
    ID = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=30)
    link = models.CharField(max_length=200)
    duration = models.IntegerField()
    productID = models.ForeignKey('Product',on_delete=models.PROTECT)

    def __str__(self):
        return self.name

class View(models.Model):
    userID = models.IntegerField()
    status = models.BooleanField()
    viewTime = models.IntegerField()
    lesson = models.ForeignKey('Lesson', on_delete=models.PROTECT)

# Создать сущность продукта. У продукта должен быть владелец.
# Необходимо добавить сущность для сохранения доступов к продукту для пользователя.
# Создать сущность урока. Урок может находиться в нескольких продуктах одновременно.
# В уроке должна быть базовая информация: название, ссылка на видео, длительность просмотра (в секундах).
# Урок могут просматривать множество пользователей.
# Необходимо для каждого фиксировать время просмотра и фиксировать статус “Просмотрено”/”Не просмотрено”.
# Статус “Просмотрено” проставляется, если пользователь просмотрел 80% ролика.
