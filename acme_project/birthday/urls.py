from django.urls import path

from . import views

app_name = 'birthday'

urlpatterns = [
    # path('путь/', views.функция_отображения, name='имя_url')
    path('', views.BirthdayCreateView.as_view(), name='create'),
    path('list/', views.BirthdayListView.as_view(), name='list'),  # Список всех дней рождений (URL: /birthday/)
    path('create/', views.birthday, name='create'),  # Создание нового дня рождения (URL: /birthday/create/)
    path('<int:pk>/edit/', views.birthday, name='edit'),  # Редактирование дня рождения с ID = pk (URL: /birthday/1/edit/)
    path('<int:pk>/delete/', views.delete_birthday, name='delete'),  # Удаление дня рождения с ID = pk (URL: /birthday/1/delete/)
]
