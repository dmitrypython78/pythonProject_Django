from django.db import models

class Task(models.Model):     #здесь наследуем все от models и дальше все от такого класса как Model
    title = models.CharField('Название', max_length= 50)
    task = models.TextField('Описание')

    def __str__(self):    #этот метод вызывается в тот момент когда мы выводим на экран обьект этого класса Task
        return self.title


    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'


