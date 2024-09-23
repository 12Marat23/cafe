from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views import View
from django.views.generic import ListView, TemplateView
from .models import *
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from .forms import *
import random


# Create your views here.

class BaseCoffeeView:
    """
    Базовый класс для представлений, связанных с отображением кофейных элементов.
    Этот класс предоставляет общую логику для получения и группировки объектов Coffees,
    а также для формирования контекста, который будет использоваться в шаблонах.
    """

    def get_grouped_coffees(self):
        """
        Возвращает список объектов Coffees, сгруппированных по 4 элемента.
        Получает все объекты Coffee из базы данных и разбивает их на группы по 4 элемента.
        Это удобно для отображения в виде карусели или сетки.
        Returns:
            list: Список списков, где каждый внутренний список содержит до 4 объектов Coffees.
        """
        coffees = Coffees.objects.all()
        grouped_coffees = [coffees[i:i + 4] for i in range(0, len(coffees), 4)]
        return grouped_coffees

    def get_context_data(self, **kwargs):
        """
        Формирует и возвращает контекст для использования в шаблоне.
        Добавляет в контекст список объектов Coffee, сгруппированных по 4 элемента.
        Args:
            **kwargs: Дополнительные аргументы ключевых слов, передаваемые в метод.
        Returns:
            dict: Контекст, который будет использоваться в шаблоне.
        """
        context = super().get_context_data(**kwargs)
        context['grouped_coffees'] = self.get_grouped_coffees()
        return context


# def index(request):
#     return render(request, 'main/index.html')

class CoffeesListView(BaseCoffeeView, ListView):
    """
    Представление списка кофе.
    Это представление наследует общую логику из BaseCoffeeView для получения и группировки объектов Coffee,
    а также использует функциональность ListView для отображения списка объектов Coffees.
    Атрибуты:
        model (Coffees): Модель, используемая для получения данных.
        template_name (str): Имя шаблона, используемого для отображения представления.
        context_object_name (str): Имя переменной контекста, в которую будут помещены объекты Coffees.
    """
    model = Coffees
    template_name = 'main/coffees.html'
    context_object_name = 'coffees'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Coffees'
        return context


class IndexView(BaseCoffeeView, TemplateView, View):
    template_name = 'main/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Home'

        comments = Comment.objects.all()
        random_comments = random.sample(list(comments), min(3, comments.count()))
        context['comments'] = random_comments
        return context

    # def get(self, request):
    #     comments = Comment.objects.all()
    #     random_comment = random.sample(list(comments), min(3, comments.count()))
    #     return render(request, 'main/index.html', {'comments': random_comment})


def about(request):
    return render(request, 'main/about.html', )


def contact_view(request):
    """
    Обрабатывает запросы на страницу контактов.
    Если метод запроса - POST, функция проверяет и обрабатывает данные формы обратной связи.
    В случае успешного завершения валидации данные сохраняются в базе данных, и пользователь
    получает сообщение об успешной отправке. В случае ошибки отображается сообщение об ошибке.
    Если метод запроса - GET, функция отображает пустую форму для ввода данных.
    Параметры:
    ----------
    request : HttpRequest
        Объект запроса, содержащий данные о методе запроса и данные формы.

    Возвращает:
    ----------
    HttpResponse
        Ответ с отрендеренной страницей контактов, содержащей форму для отправки сообщений.
    """
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()  # Сохранение сообщения в базу данных
            messages.success(request, 'Сообщение отправлено')  # Перенаправление на страницу успеха
            return redirect('contact')
        else:
            messages.error(request, 'Ошибка')
    else:
        form = ContactForm()
    return render(request, 'main/contact.html', {'form': form})
