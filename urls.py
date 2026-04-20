from django.urls import path
from student.views import registration, login, address


urlpatterns = [
    path('register/', registration, name='registration'),
    path('login/', login, name='login'),
    path('address/', address, name='address'),

]