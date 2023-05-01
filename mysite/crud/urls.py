from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name=''),
    path('form/', views.form, name='form'),
    path('<int:id>/', views.form, name='update'),
    path('show/', views.show, name='show'),
    path('delete/<int:id>/', views.delete, name='delete')
       
]