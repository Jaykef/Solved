from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('darkmode/', views.index_dark, name='home_dark')
]
