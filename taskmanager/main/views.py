from django.shortcuts import render
from .models import Task
from .forms import TaskForm


def index(request):
    tasks = Task.objects.all()
    #если хотим отсортировать все записи по определенному полю, можно использовать функцию order_by
    # tasks = Task.objects.order_by('id') #в скобках указывам по какому полю хотим сортировать напр: по полю ('tasks'), или по ('title')
    # так же можно сортировать по полю ('id')
    # tasks = Task.objects.order_by('-id') #если перед id указываем '-', это значит, что сортировка будет произведена в обратном порядке
    # tasks = Task.objects.order_by('id') [:1] если указать срез, это будет значить, что отсортировать лишь одну запись,  [:5]- пять записей
    return render(request, 'main/index.html', {'title': 'Главная страница сайта', 'tasks': tasks})


def about(request):
    tasks = Task.objects.all()
    return render(request, 'main/about.html', {'title': 'О нас', 'tasks': tasks})


def price(request):
    tasks = Task.objects.all()
    return render(request, 'main/price.html', {'title': 'Прайс', 'tasks': tasks})

def contact (request):
    tasks = Task.objects.all()
    return render(request, 'main/contact.html', {'title': 'Контакты', 'tasks': tasks})


def create(request):
    form = TaskForm()
    context = {
        'form': form

    }
    tasks = Task.objects.all()
    return render(request, 'main/create.html', {'title': 'О нас', 'tasks': tasks})

