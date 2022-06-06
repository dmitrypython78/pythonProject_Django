#Эта форма будет работать с определенной моделью
from .models import Task
from django.forms import ModelForm, TextInput, Textarea

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ("title", "task")       #filds это ключ, в котором мы указываем какие поля должны присутствовать в нашей форме
        widgets = {
            "title": Textarea(attrs={
                'class': 'form-control',
                'plaseholder': 'Введите  описание'
            }),
        }