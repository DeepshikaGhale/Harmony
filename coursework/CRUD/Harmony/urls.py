from django.urls import path 
from . import views

urlpatterns = [
    path('',views.lyrics, name='lyrics')

]