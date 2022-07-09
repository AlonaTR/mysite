from django.urls import path, converters
from numpy import sign
from .views import *

urlpatterns = [
    path('', index),
    path('<int:month>/<int:day>', month_day_horoscope),
    path('type/<str:type>/', type_of_horoscope, name='type_horoscope'),
    path('<int:sign>/', info_about_horoscope_number ),
    path('<str:sign_zodiac>/', info_about_horoscope,name='horoscope_name'),
    
]