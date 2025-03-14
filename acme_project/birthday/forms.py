# birthday/forms.py
from django import forms
from django.core.exceptions import ValidationError
from .models import Birthday
from .validators import real_age
from django.db import models

BEATLES = {'Джон Леннон', 'Пол Маккартни', 'Джордж Харрисон', 'Ринго Старр'}

class BirthdayForm(forms.ModelForm):
    class Meta:
        model = Birthday  # Указываем модель, с которой связана форма
        fields = '__all__'
        widgets = {
            'birthday': forms.DateInput(attrs={'type': 'date'})
        }
        constraints = (
            models.UniqueConstraint(
                fields=('first_name', 'last_name', 'birthday'),
                name='Unique person constraint',
            ),
        )   # Или перечислите нужные поля
        # constraints - нельзя использовать здесь!

    def clean_first_name(self):
        first_name = self.cleaned_data['first_name']
        return first_name.split()[0]

    def clean(self):
        super().clean()  # Сначала вызываем родительский метод clean
        first_name = self.cleaned_data.get('first_name')  # Используем get()
        last_name = self.cleaned_data.get('last_name')    # Используем get()

        if first_name and last_name:  # Проверяем, что поля существуют
            if f'{first_name} {last_name}' in BEATLES:
                raise ValidationError(
                    'Мы тоже любим Битлз, но введите пожалуйста настоящее имя!'
                )