from django.urls import path
from .views import contact,fedback 
    
urlpatterns = [  
    path("contact/",contact,name='contact'),
    path("feedback/",fedback,name='feedback')

]