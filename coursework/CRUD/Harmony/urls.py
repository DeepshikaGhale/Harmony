from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [ 
    path('',view_Music_page),
    path('save',view_Musicdata_save),
    path('Musicdata/',view_Music_lists), 
    path('Musicform/',view_Music_form),
    path('Musicdata/edit/<int:ID>',view_Musicdata_updateform),
    path('Musicdata/edit/update/<int:ID>',view_update_form_data_in_db),
]