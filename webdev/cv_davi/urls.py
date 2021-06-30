from django.urls import path

from webdev.cv_davi import views

app_name = 'cv_davi'

urlpatterns = [
    path('', views.home, name='home')
]
