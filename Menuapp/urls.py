from django.urls import path
from .views import menu

app_name = 'Menuapp'


urlpatterns = [
    path('menu/', menu, name='menu'),

]

