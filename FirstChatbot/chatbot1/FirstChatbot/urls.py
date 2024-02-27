from django.urls import path 
from . import views

urlpatterns = [
    path('',views.FirstChatbot, name='chatbot')
]

