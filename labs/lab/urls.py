from django.urls import path
from . import views

app_name = 'lab'

urlpatterns = [
    path('', views.index, name="index"),
    path('greetings/', views.greetings, name="greetings"),
    path('now/', views.current_datetime, name="now"),
    path('get_xkcd/', views.xkcd, name="get_xkcd"),
    path('random_dog', views.random_dog, name='random_dog'),
    path('get_dog', views.get_dog, name='get_dog'),
    path('generate_qr_code', views.generate_qr_code, name='generate_qr_code')
]
