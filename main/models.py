from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    name = models.CharField('Название', max_length=20)
    description = models.CharField('Описание', max_length=150)

    def __str__(self):
        return self.name
