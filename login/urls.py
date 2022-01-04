from django.urls import path
from.views import singin,registernew,register

urlpatterns = [

    path('singin/',singin,name='singin'),
    path('registernew/',registernew,name='registernew'),
    path('register/',register,name='register'),

]