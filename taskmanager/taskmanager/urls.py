
from django.contrib import admin
from django.urls import path, include



urlpatterns = [
    path('admin/', admin.site.urls),    #отслеживаем переход на страницу админ
    path('', include('main.urls')),     #отслеживаем переход на главную страницу. Пустая строка подразумевает переход на главную


]
