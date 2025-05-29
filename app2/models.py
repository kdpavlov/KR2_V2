from django.db import models

# Create your models here.

class Page(models.Model):
    title = models.CharField("Заголовок", max_length=200, unique=True)
    content = models.TextField("Контент")
    updated = models.DateTimeField("Дата обновления", auto_now=True)

    def __str__(self):
        return self.title

class Student(models.Model):
        full_name = models.CharField("ФИО", max_length=200)
        photo = models.ImageField("Фото", upload_to='students/')
        email = models.EmailField("Email")
        phone = models.CharField("Телефон", max_length=20)
        score = models.PositiveIntegerField("Баллы", default=0)

        def __str__(self):
            return self.full_name

