from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:journey_id>/', views.detail, name='detail'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about')
]
