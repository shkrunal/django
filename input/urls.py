from django.urls import path
from .views import contact,fedback,calculator
    
urlpatterns = [  
    path("contact/",contact,name='contact'),
    path("feedback/",fedback,name='feedback'),
    path('cal/',calculator,name='cal')
]