from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import ListView
from .models import Coffees, ContactMessage
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from .forms import *


# Create your views here.

def index(request):
    return render(request, 'main/index.html')


def about(request):
    return render(request, 'main/about.html')


class CoffeesListView(ListView):
    model = Coffees
    template_name = 'main/coffees.html'
    context_object_name = 'coffees'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Coffees'
        return context


# def coffees(request):
#     return render(request, 'main/coffees.html')


# def contact(request):
#     return render(request, 'main/contact.html')


@csrf_exempt
def contact_view(request):

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()  # Сохранение сообщения в базу данных
            messages.success(request, 'Сообщение отправлено')  # Перенаправление на страницу успеха
            return redirect('contact')
        else: messages.error(request, 'Ошибка')
    else:
        form = ContactForm()
    return render(request, 'main/contact.html', {'form': form})
