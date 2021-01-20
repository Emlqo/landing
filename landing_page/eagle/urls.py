from django.urls import path

from . import views
app_name ='eagle'
urlpatterns = [
    path('', views.index, name='index'),
    path('<str:Email>/', views.email, name='email'),
]