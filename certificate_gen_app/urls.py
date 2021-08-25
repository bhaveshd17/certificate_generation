from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add_template/', views.add_template, name='add_template')

]