from django.shortcuts import get_object_or_404, redirect, render

from .forms import BirthdayForm
from .models import Birthday
from .utils import calculate_birthday_countdown
from django.core.paginator import Paginator
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from django.views.generic.edit import FormMixin


class BirthdayMixin:
    model = Birthday
    success_url = reverse_lazy('birthday:list')  # добавляем success_url


class BirthdayFormMixin(FormMixin):  # меняем наследование
    form_class = BirthdayForm
    template_name = 'birthday/birthday.html'


class BirthdayCreateView(BirthdayMixin, BirthdayFormMixin, CreateView):
    template_name = 'birthday/birthday.html'
    form_class = BirthdayForm

    def form_valid(self, form):
        # Вызываем родительский метод для сохранения данных
        response = super().form_valid(form)
        # Получаем данные из формы
        birthday_value = form.cleaned_data['birthday']
        # Вычисляем обратный отсчет
        birthday_countdown = calculate_birthday_countdown(birthday_value)
        # Добавляем countdown в контекст
        self.object.countdown = birthday_countdown
        # Сохраняем объект
        self.object.save()
        return response


class BirthdayUpdateView(BirthdayMixin, BirthdayFormMixin, UpdateView):
    template_name = 'birthday/birthday.html'
    form_class = BirthdayForm

    def form_valid(self, form):
        # Вызываем родительский метод для сохранения данных
        response = super().form_valid(form)
        # Получаем данные из формы
        birthday_value = form.cleaned_data['birthday']
        # Вычисляем обратный отсчет
        birthday_countdown = calculate_birthday_countdown(birthday_value)
        # Добавляем countdown в контекст
        self.object.countdown = birthday_countdown
        # Сохраняем объект
        self.object.save()
        return response


class BirthdayDeleteView(BirthdayMixin, DeleteView):
    template_name = 'birthday/birthday_confirm_delete.html'
    success_url = reverse_lazy('birthday:list')


class BirthdayListView(ListView):
    model = Birthday
    template_name = 'birthday/birthday_list.html'
    context_object_name = 'birthdays'
    paginate_by = 4


class BirthdayDetailView(DetailView):
    model = Birthday

    def get_context_data(self, **kwargs):
        # Получаем словарь контекста:
        context = super().get_context_data(**kwargs)
        # Добавляем в словарь новый ключ:
        context['birthday_countdown'] = calculate_birthday_countdown(
            # Дату рождения берём из объекта в словаре context:
            self.object.birthday
        )
        # Возвращаем словарь контекста.
        return context 