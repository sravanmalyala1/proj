from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('my-view/', views.my_view, name='my_view'),
    path('my-view1/', views.my_view1, name='my_view'),
]
