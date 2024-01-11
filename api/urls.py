from django.urls import path
from . import views

urlpatterns =  [
    path('api/create_collection/', views.create_collection, name='create_collection'),
    path('api/add_questions/', views.add_questions, name='add_questions'),

]