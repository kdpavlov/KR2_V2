from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class Person(models.Model):
    full_name = models.CharField(verbose_name='Имя', max_length=255)
    email = models.EmailField(verbose_name='Почта')
    phone = models.CharField(verbose_name='Телефон',max_length=15)
    photo = models.ImageField(verbose_name='Фото',upload_to='photos/')
    resume = RichTextField(verbose_name='Резюме')

    def str(self):
        return self.full_name

class Management(models.Model):
    leader = models.ForeignKey(Person, related_name="leader", on_delete=models.CASCADE)
    managers = models.ManyToManyField(Person, related_name="managers", verbose_name='Менеджеры')

    def str(self):
        return f"Management for {self.leader.full_name}"

class Page(models.Model):
    title = models.CharField("Заголовок", max_length=200, unique=True)
    content = models.TextField("Контент")
    updated = models.DateTimeField("Дата обновления", auto_now=True)

    def __str__(self):
        return self.title

class Student(models.Model):
    full_name = models.CharField("ФИО", max_length=200)
    photo = models.ImageField("Фото", upload_to='')
    email = models.EmailField("Email")
    phone = models.CharField("Телефон", max_length=20)
    score = models.PositiveIntegerField("Баллы", default=0)

    def __str__(self):
        return self.full_name

class Program(models.Model):
    name = models.CharField("Имя", max_length=255)
    description = RichTextField("Описание")
    benefits = RichTextField("Преимущества")
    link = models.URLField("Ссылка")

    def str(self):
        return self.name

