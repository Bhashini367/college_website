from django.urls import path
from . import views

urlpatterns = [
    path('boot/', views.boot, name='boot'),
    path('', views.home, name='home'),
    path('students/', views.students, name='students'),
    path('colleges/', views.colleges, name='colleges'),
    path('address/', views.address, name='address'),
    path('email/',views.send_email,name='send_email')
]
