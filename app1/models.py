from django.db import models

# Create your models here.
class StudyRecord(models.Model):
    name = models.CharField(max_length=100)  # Имя
    course = models.CharField(max_length=100)  # Название курса
    score = models.IntegerField()  # Оценка, баллы
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.course} ({self.score})"