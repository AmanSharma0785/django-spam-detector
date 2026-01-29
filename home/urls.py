from django.urls import path
from . import views

urlpatterns = [  
    path('', views.spam_check, name='spam_check')
    
]